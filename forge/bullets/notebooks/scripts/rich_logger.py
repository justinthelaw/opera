from rich.table import Column, Table
from rich.console import Console
from rich.live import Live


class TrainingTable:
    def __init__(self):
        self.table = Table(
            Column("Epoch", justify="left"),
            Column("Loss Rate", justify="left"),
            title="Training Status",
        )
        self.epoch_refresh = True

    def add_row(self, epoch, loss):
        """
        The function "add_row" adds a new row to a table with the given epoch and loss values.

        :param epoch: The epoch parameter represents the current epoch number. In machine learning, an epoch
        refers to one complete pass through the entire training dataset. It is used to track the progress of
        the training process
        :param loss: The "loss" parameter represents the loss value for a particular epoch. Loss is a
        measure of how well a machine learning model is performing on a given task. It quantifies the
        difference between the predicted output of the model and the actual output. The lower the loss
        value, the better the model is
        """
        self.table.add_row(str(epoch + 1), str(loss))

    def get_table(self):
        """
        The function returns the value of the "table" attribute.
        :return: The `get_table` method is returning the `table` attribute.
        """
        return self.table

    def get_epoch_refresh(self):
        """
        The function `get_epoch_refresh` returns the value of the `epoch_refresh` attribute.
        :return: The method is returning the value of the variable `self.epoch_refresh`.
        """
        return self.epoch_refresh

    def refresh_table(self, epoch, total_loss):
        """
        The function refreshes a table with the given epoch and total loss values.

        :param epoch: The epoch parameter represents the current epoch number during training. An epoch is a
        complete pass through the entire training dataset
        :param total_loss: The total loss is a measure of how well the model is performing during training.
        It is typically calculated as the average loss over a batch or an epoch. The lower the total loss,
        the better the model is performing
        """
        self.add_row(epoch, total_loss)
        live_refresher.update(training_table.get_table(), refresh=True)
        self.epoch_refresh = False

    def switch_epoch_refresh(self):
        """
        The function `switch_epoch_refresh` sets the `epoch_refresh` attribute to `True`.
        """
        self.epoch_refresh = True


# Define a rich console logger
general_logger = Console(record=False)

# Instantiate new training table
training_table = TrainingTable()

# Instantiate the table's live refreshing wrapper
live_refresher = Live(training_table.get_table(), console=general_logger, auto_refresh=False)
