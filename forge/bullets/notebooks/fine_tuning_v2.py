# forge/bullets/notebooks/auto_fine_tune.py

from rich.console import Console
from rich.live import Live
from rich.table import Table, Column
from forge.bullets.notebooks.scripts.rich_logger import TrainingTable

def auto_fine_tune():
    """
    Function to perform fine-tuning using Hugging Face's Auto* methods.
    """
    # Add in-line comments to outline each step's purpose
    # ...

    # Use Hugging Face's Auto* methods for fine-tuning
    # ...

    # Extract epoch and loss at each training interval using TrainingTable class
    # ...

    # Include validation step using 15% of training data and calculate ROUGE scores
    # ...