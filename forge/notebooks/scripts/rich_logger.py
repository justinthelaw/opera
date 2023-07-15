from rich.table import Column, Table
from rich import box
from rich.console import Console

# Define a rich console logger
general_logger = Console(record=True)

training_logger = Table(
    Column("Epoch", justify="center"),
    Column("Steps", justify="center"),
    Column("Loss", justify="center"),
    title="Training Status",
    pad_edge=False,
    box=box.ASCII,
)
