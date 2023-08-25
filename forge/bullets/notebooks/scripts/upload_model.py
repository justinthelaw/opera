import os
from transformers import TrainingArguments, Trainer
from loguru import logger


# You must be logged-in on your transformers CLI already
def upload_to_huggingface(
    directory: str, model_name: str, model_type: str, repository_url: str
):
    """
    The `upload_to_huggingface` function takes in a directory path, model name, model type, and
    the repository URL, then uploads the model artifacts to an existing Hugging Face repository.

    :param directory: The directory where the model artifacts are located.
    :type directory: str
    :param model_name: Desired name for your model on Hugging Face's model hub.
    :type model_name: str
    :param model_type: The type of model architecture you are using (e.g., 't5', 'bert').
    :type model_type: str
    :param repository_url: The URL of the existing repository on Hugging Face Hub.
    :type repository_url: str
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise ValueError(f"The directory {directory} does not exist!")

        # Change working directory
        os.chdir(directory)

        # Push to Hugging Face
        training_args = TrainingArguments(output_dir="./", overwrite_output_dir=True)
        trainer = Trainer(args=training_args)
        trainer.push_to_hub(
            model_name, repo_type=model_type, repository_url=repository_url
        )

        logger.success("Successfully uploaded the model to Hugging Face Hub!")

    except Exception as e:
        logger.error(f"Error occurred: {e}")


if __name__ == "__main__":
    dir_path = input(
        "Enter the relative path to the directory with model artifacts: "
    )
    model_name = input(
        "Enter the desired model name in the format 'username/model_name': "
    )
    model_type = input("Enter the model type (e.g., 't5', 'bert'): ")
    repo_url = input(
        "Enter the URL of the existing repository on Hugging Face Hub: "
    )

    upload_to_huggingface(dir_path, model_name, model_type, repo_url)
