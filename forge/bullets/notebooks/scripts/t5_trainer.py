import torch
import numpy as np
from torch.utils.data import DataLoader
from transformers import get_linear_schedule_with_warmup
from loguru import logger

from scripts.constants import *
from scripts.model_instantiation import *
from scripts.rich_logger import live_refresher
from scripts.dataset import CustomDataset
from scripts.training import train, save_trained_model
from scripts.validation import rouge_validation


# T5 training main function
def T5Trainer(
    model, tokenizer, model_output_directory, dataframe, source_text, target_text
):
    try:
        # Set random seeds and deterministic pytorch for reproducibility
        torch.manual_seed(seed)
        np.random.seed(seed)
        torch.backends.cudnn.deterministic = True  # type: ignore

        logger.info("Reading data...")
        # Importing the raw dataset
        dataframe = dataframe[[source_text, target_text]]

        # Creation of Dataset and Dataloader
        # 80% of the data will be used for training and the rest for validation
        train_size = training_validation_split
        train_dataset = dataframe.sample(frac=train_size, random_state=seed)
        val_dataset = dataframe.drop(train_dataset.index).reset_index(drop=True)
        train_dataset = train_dataset.reset_index(drop=True)

        logger.info(f"FULL Dataset: {dataframe.shape}")
        logger.info(f"TRAIN Dataset: {train_dataset.shape}")
        logger.info(f"VALIDATION Dataset: {val_dataset.shape}")

        # Creating the Training and Validation dataset for further creation of data loader
        training_set = CustomDataset(
            train_dataset,
            tokenizer,
            max_input_token_length,
            max_output_token_length,
            source_text,
            target_text,
        )
        val_set = CustomDataset(
            val_dataset,
            tokenizer,
            max_input_token_length,
            max_output_token_length,
            source_text,
            target_text,
        )

        # Defining the parameters for creation of data loaders
        train_params = {
            "batch_size": train_batch_size,
            "shuffle": True,
            "num_workers": 0,
        }
        val_params = {
            "batch_size": valid_batch_size,
            "shuffle": False,
            "num_workers": 0,
        }

        # Creation of data loaders for testing and validation - this will be used down for training and validation stage for the model
        training_loader = DataLoader(training_set, **train_params)
        val_loader = DataLoader(val_set, **val_params)

        # Defining the optimizer that will be used to tune the weights of the network in the training session
        optimizer = torch.optim.AdamW(
            params=[p for p in model.parameters() if p.requires_grad],
            lr=learning_rate,
            eps=adam_epsilon,
            weight_decay=weight_decay,
        )

        # Define the learning rate scheduler
        scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps=train_epochs
            * len(training_loader)
            // gradient_accumulation_steps,
        )

        # Training loop
        logger.info(f"Initiating T5x variant fine tuning...")
        # Table logger for training statistics
        with live_refresher:
            for epoch in range(train_epochs):
                train(epoch, tokenizer, model, training_loader, optimizer, scheduler)
        logger.info(f"Saving fine-tuned  to {model_output_directory} ...")
        # Saving the model after training
        save_trained_model(model, tokenizer, model_output_directory)

        # Evaluating validation dataset
        logger.info("Initiating validation...")
        for _ in range(val_epochs):
            rouge_validation(tokenizer, model, val_loader)
        logger.success("Model fine tuning, saving, and validation steps completed!")

    except Exception as e:
        # Handle other unexpected errors
        logger.error(f"An unexpected error occurred during fine tuning: {str(e)}")
        # Save the model and any relevant data before exiting gracefully
        save_trained_model(model, tokenizer, model_output_directory)
