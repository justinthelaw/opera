# Import necessary libraries
from transformers import AutoModel, AutoTokenizer, T5ForConditionalGeneration, Seq2SeqTrainingArguments, Trainer
import torch
from loguru import logger
from rich import print

# Define global parameters
max_input_token_length = 512
max_output_token_length = 128
number_of_beams = 2

# Load pre-trained model and tokenizer
model_name = input("What is the target model's checkpoint name on Hugging Face?")
directory_path = f"../models/{model_name}"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Save the model and tokenizer to your specified directory
tokenizer.save_pretrained(directory_path)
model.save_pretrained(directory_path)

# Fine-tune the model
# Ask the user for the path to the training dataset
dataset_path = input("What is the path to the training dataset?")
# Load the training dataset from the specified file
# This is a placeholder. The actual code will depend on the format of your dataset.
training_dataset = torch.load(dataset_path)
# Create a Seq2SeqTrainingArguments object
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
)
# Create a Trainer object with the model, training arguments, and training dataset
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=training_dataset,
)
# Call the train method on the Trainer object to fine-tune the model
trainer.train()
print("Fine-tuning model...")