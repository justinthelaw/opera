import torch
from transformers import T5ForConditionalGeneration
from torch.utils.data import DataLoader
import sys
from torch.utils.data import Dataset, DataLoader


class PreparedDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def train_t5_model(model, data_loader, optimizer, scheduler, device, epochs):
    model.to(device)
    model.train()
    for epoch in range(epochs):
        total_loss = 0

        for batch in data_loader:
            batch_input_ids = batch["input_ids"].to(device)
            batch_labels = batch["labels"].to(device)

            # Forward pass
            outputs = model(input_ids=batch_input_ids, labels=batch_labels)
            loss = outputs.loss
            total_loss += loss.item()

            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            scheduler.step()

        average_loss = total_loss / len(data_loader)
        print(f"Epoch {epoch + 1} - Average Loss: {average_loss}")


def main():
    # Parse the command-line arguments
    epochs = int(sys.argv[1])
    learning_rate = float(sys.argv[2])
    total_steps = int(sys.argv[3])

    # Convert the dataset into a PyTorch DataLoader
    batch_size = 8
    dataset = PreparedDataset(prepared_data)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Initialize the T5 model
    model = T5ForConditionalGeneration.from_pretrained("t5-base")

    # Set up the optimizer and scheduler
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    """
    Learning rate scheduling strategy notes:
        max_lr: The maximum learning rate used during training - helps control the learning rate range during the training process
        total_steps: The total number of steps in the training process - influences the scheduling of the learning rate and momentum during training
        div_factor: The factor by which the initial learning rate is divided to get the lower boundary learning rate - affects the lower bound of the learning rate range
        final_div_factor: The factor by which the initial learning rate is divided to get the final learning rate - affects the final learning rate at the end of the training process
        pct_start: The percentage of the total number of steps used for the warm-up phase - determines the portion of the training where the learning rate gradually increases
        anneal_strategy: The strategy used for annealing the learning rate and momentum during training - set to "cos" for cosine annealing
        cycle_momentum: Whether to cycle the momentum between base_momentum and max_momentum during training
        base_momentum: The lower momentum boundary during training
        max_momentum: The upper momentum boundary during training
        epochs: The number of epochs to train the model
        steps_per_epoch: The number of steps per epoch - used to calculate the learning rate schedule
        warmup_steps: The number of warm-up steps where the learning rate gradually increases - helps the model to stabilize at the beginning of training
    """
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer,
        max_lr=learning_rate,
        total_steps=total_steps,
        div_factor=2.0,
        final_div_factor=1e4,
        pct_start=0.1,
        anneal_strategy="cos",
        cycle_momentum=True,
        base_momentum=0.85,
        max_momentum=0.95,
        epochs=epochs,
        steps_per_epoch=len(data_loader),
    )

    # Training loop
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_t5_model(model, data_loader, optimizer, scheduler, device, epochs)

    # Save the trained model
    output_model = "trained_model.pt"  # Specify the output file name
    model.save_pretrained(output_model)


if __name__ == "__main__":
    main()
