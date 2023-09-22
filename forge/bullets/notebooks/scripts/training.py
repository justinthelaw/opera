import re
import torch
from loguru import logger
from torch.cuda.amp.grad_scaler import GradScaler

from scripts.constants import *
from scripts.rich_logger import training_table as table


# Saves the model
def save_trained_model(model, tokenizer, model_output_directory):
    model.save_pretrained(model_output_directory)
    tokenizer.save_pretrained(model_output_directory)
    logger.info(f"Fine-tuned model successfully saved to: {model_output_directory}")
    logger.success("Model saved. Shutting down...")


# Generates a penalty for not complying to bullet formatting
def bullet_format_penalty(outputs, tokenizer, format_pattern):
    total_penalty = 0.0
    logits = outputs.logits
    # Converting the logits to token ids
    token_ids = torch.argmax(logits, dim=-1)
    # Decoding the token ids to text
    decoded_outputs = [
        tokenizer.decode(token_ids[i], skip_special_tokens=True)
        for i in range(token_ids.shape[0])
    ]

    for text in decoded_outputs:
        match = re.fullmatch(format_pattern, text)
        # If the output does not match the desired format exactly, add a penalty
        if not match:
            total_penalty += 1.0

    return torch.tensor(total_penalty, device=logits.device)


# function to be called for training with the parameters passed from main function
def train(epoch, tokenizer, model, loader, optimizer, scheduler):
    # create a GradScaler object for mixed precision training
    # optionally define the GradScaler based on cuda availability
    use_cuda = torch.cuda.is_available()
    scaler = GradScaler(enabled=use_cuda) if use_cuda else None

    # training logger refresh flag
    table.switch_epoch_refresh()
    # stepping through training batches, where loader is the dataloader from pytorch
    for step, data in enumerate(loader, 0):
        # move target ids (ground truth) to the specified device (e.g., gpu) and data type (long)
        y = data["target_ids"].to(device, dtype=torch.long)
        # extract y_ids by excluding the last token (used for training language model)
        y_ids = y[:, :-1].contiguous()
        # clone and detach y to create the lm_labels (used for masked language model loss)
        lm_labels = y[:, 1:].clone().detach()
        # replace positions with padding tokens in lm_labels with -100 (masked lm loss)
        lm_labels[y[:, 1:] == tokenizer.pad_token_id] = -100
        # move source ids to the specified device and data type (used for input)
        ids = data["source_ids"].to(device, dtype=torch.long)
        # move source mask to the specified device and data type (used for attention mask)
        mask = data["source_mask"].to(device, dtype=torch.long)

        outputs = model(
            input_ids=ids,
            attention_mask=mask,
            decoder_input_ids=y_ids,
            labels=lm_labels,
        )
        loss = outputs[0]

        # add a penalty to the loss for outputs that don't match the format
        format_loss = bullet_format_penalty(outputs, tokenizer, bullet_pattern)
        total_loss = loss + format_loss

        if table.get_epoch_refresh():
            # refresh table once per epoch
            table.refresh_table(epoch, loss)

        if scaler:  # If CUDA is available and scaler is defined
            scaler.scale(total_loss).backward()  # type: ignore

            if (step + 1) % gradient_accumulation_steps == 0:
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # type: ignore
                scaler.step(optimizer)
                scaler.update()

                # Clear gradients after optimizer step
                optimizer.zero_grad()
        else:  # If no CUDA, follow standard backward pass
            total_loss.backward()

            if (step + 1) % gradient_accumulation_steps == 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # type: ignore
                optimizer.step()

                # Clear gradients after optimizer step
                optimizer.zero_grad()

        # Adjust the learning rate
        scheduler.step()
