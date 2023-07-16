from rich.table import Column, Table
from rich.console import Console
from rich.live import Live

# Training table class
class TrainingTable:
    def __init__(self):
        self.table = Table(
            Column("Epoch", justify="left"),
            Column("Loss Rate", justify="left"),
            title="Training Status",
        )
        self.epoch_refresh = True

    def add_row(self, epoch, loss):
        self.table.add_row(str(epoch + 1), str(loss))

    def get_table(self):
        return self.table

    def get_epoch_refresh(self):
        return self.epoch_refresh

    def refresh_table(self, epoch, total_loss):
        self.add_row(epoch, total_loss)
        live_refresher.update(training_table.get_table(), refresh=True)
        self.epoch_refresh = False

    def switch_epoch_refresh(self):
        self.epoch_refresh = True


# Define a rich console logger
general_logger = Console(record=False)

# Instantiate new training table
training_table = TrainingTable()

# Generate new live logging instance
live_refresher = Live(
    training_table.get_table(), console=general_logger, auto_refresh=False
)
