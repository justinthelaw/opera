from rich.console import Console
from rich.live import Live
from rich.table import Table, Column

from rich_logger import TrainingTable

# Instantiate a rich console logger
console = Console(record=False)

# Instantiate a training table
training_table = TrainingTable()

# Generate a live logging instance
live_refresher = Live(training_table.get_table(), console=console, auto_refresh=False)

# Add in-line comments to outline each step's purpose
# Step 1: Load the NLP model
# Step 2: Prepare the training data
# Step 3: Define the optimizer and loss function
# Step 4: Train the model
# Step 5: Extract epoch and loss values at each training interval
for epoch in range(num_epochs):
    # Training loop
    for batch in training_data:
        # Perform training steps

        # Update the training table with epoch and loss values
        training_table.add_row(epoch, loss)

    # Refresh the table and update the live logging instance
    live_refresher.update(training_table.get_table(), refresh=True)

# Switch off epoch refresh
training_table.switch_epoch_refresh()

# Add validation step using 15% of the training data and calculate ROUGE scores
# Step 6: Prepare the validation data
# Step 7: Perform validation and calculate ROUGE scores

# Switch on epoch refresh
training_table.switch_epoch_refresh()

# Refresh the table and update the live logging instance
live_refresher.update(training_table.get_table(), refresh=True)

# Close the live logging instance
live_refresher.close()