# This is the regex for a standard bullet pattern "-[ACTION];[IMPACT]--[OUTCOME]"
# The pattern is not all-encompassing - this hardcoded value can to be experimented with
# to achieve maximum bullet capture
bullet_pattern = r"^-?([\w\W\s]{0,255});?([\w\W\s]{0,255})--([\w\W\s]{0,255})$"
# Input prefix used for fine tuning the model to comprehend as a key word for
# bullet creation tasking
bullet_prompt_prefix = (
    "Using the following Air and Space Force bullet statement format, where special characters are always of the same exact order and type, "
    + "`- [ACTION]; [IMPACT]--[RESULT] `, write an Air and Space Force bullet statement from the following details: "
)
# Input prefix used for fine tuning the model to comprehend as a key word for
# bullet creation tasking
bullet_data_creation_prefix = "Using full sentences, expand upon the following Air and Space Force bullet statement by spelling-out acronyms and adding additional context: "
# Max length of tokens a user may enter for summarization
# Increasing this beyond 512 may increase compute time significantly
max_input_token_length = 512
# Max length of tokens the model should output for the summary
# Approximately the number of tokens it may take to generate a bullet
max_output_token_length = 512
# Beams to use for beam search algorithm
# Increased beams means increased quality, but increased compute time
number_of_beams = 6
# Number of examples per batch during training
# Larger batch sizes require more memory, but can speed up training
train_batch_size = 1
# Number of full passes through the entire training dataset
# More epochs can lead to better performance, but risk over-fitting
train_epochs = 6
# Number of examples per batch during validation
# Larger batch sizes require more memory, but can speed up the validation process
valid_batch_size = 1
# Number of full passes through the entire validation dataset
# Typically kept to a single epoch as the validation set does not need to be repeatedly passed
val_epochs = 1
# Affects how quickly or slowly a model learns
# Too high can cause instability, too low can cause slow learning
learning_rate = 1e-4
# Random seed to ensure reproducibility
# Using the same seed will yield the same model given the same data and training process
seed = 8
# Multiplier to penalize repeated n-grams
# Higher values discourage repetition in the generated text
repetition_penalty = 1
# Penalty applied for producing long sequences
# Higher values encourage longer sequences
length_penalty = 0
# The number of steps to take before the gradient is averaged and applied
# Helps in stabilizing training and requires less memory
gradient_accumulation_steps = 1
# Weight decay introduced to the optimizer to prevent over-fitting
# Regularization strategy by adding a small penalty, typically the L2 norm of the weights
weight_decay = 0.1
# Small constant to prevent any division by zero in the implementation (Adam)
adam_epsilon = 1e-8
# Number of steps for the warmup phase
# Helps in avoiding very high and undesirable values of gradients at the start of training
warmup_steps = 4
# The split between the training and validation data
training_validation_split = 0.85
# Scales logits before soft-max to control randomness
# Lower values (~0) make output more deterministic
temperature = 0.5
# Limits generated tokens to top K probabilities
# Reduces chances of rare word predictions
top_k = 50
# Applies nucleus sampling, limiting token selection to a cumulative probability
# Creates a balance between randomness and determinism
top_p = 0.90
