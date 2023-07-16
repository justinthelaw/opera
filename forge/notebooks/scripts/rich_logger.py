from rich.table import Column, Table
from rich import box
from rich.console import Console
from rich.live import Live


class TrainingTable:
    def __init__(self):
        self.table = Table(
            Column("Epoch", justify="left"),
            Column("Steps", justify="left"),
            Column("Loss, Calculator", justify="left"),
            title="Training Status",
            padding=2,
            expand=True,
            pad_edge=True,
            box=box.ROUNDED,
        )

    def add_row(self, epoch, steps, loss):
        # Add row to the table
        self.table.add_row(str(epoch + 1), str(steps + 1), str(loss))

    def get_table(self):
        # Return current state of the table
        return self.table


# Define a rich console logger
general_logger = Console(record=False, highlight=False)

# Instantiate new training table
training_table = TrainingTable()

# Generate new live logging instance
live_refresher = Live(training_table, console=general_logger, auto_refresh=False)
