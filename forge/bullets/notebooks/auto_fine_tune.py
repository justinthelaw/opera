import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
import logging
from transformers import TrainingArguments, Trainer

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fine_tune_model(model_name, train_dataset, validation_dataset, output_dir):
    """
    Fine-tunes the NLP model using the provided train and validation datasets.
    
    Args:
        model_name (str): The name of the pre-trained model to be fine-tuned.
        train_dataset (Dataset): The training dataset.
        validation_dataset (Dataset): The validation dataset.
        output_dir (str): The directory to save the fine-tuned model.
    """
    # Load the pre-trained model and tokenizer
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Configure the model for fine-tuning
    config = AutoConfig.from_pretrained(model_name)
    config.num_labels = len(train_dataset.labels)
    model.config = config
    
    # Tokenize the input data
    train_encodings = tokenizer(train_dataset.texts, truncation=True, padding=True)
    val_encodings = tokenizer(validation_dataset.texts, truncation=True, padding=True)
    
    # Prepare the data for training
    train_dataset = torch.utils.data.TensorDataset(
        torch.tensor(train_encodings.input_ids),
        torch.tensor(train_encodings.attention_mask),
        torch.tensor(train_dataset.labels)
    )
    val_dataset = torch.utils.data.TensorDataset(
        torch.tensor(val_encodings.input_ids),
        torch.tensor(val_encodings.attention_mask),
        torch.tensor(validation_dataset.labels)
    )
    
    # Set up the training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir=output_dir,
        logging_steps=10,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=3,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        greater_is_better=True
    )
    
    # Create the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics
    )
    
    # Fine-tune the model
    trainer.train()
    
    # Save the fine-tuned model
    trainer.save_model(output_dir)
    
    logger.info(f"Fine-tuned model saved to {output_dir}")

if __name__ == "__main__":
    # Define the train and validation datasets
    train_dataset = ...
    validation_dataset = ...
    
    # Fine-tune the model
    fine_tune_model(model_name, train_dataset, validation_dataset, output_dir)
