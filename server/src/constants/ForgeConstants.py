import os

# Base model constants
MODEL = os.getenv("BULLET_MODEL", "google/flan-t5-base")
TOKENIZER = os.getenv("BULLET_TOKENIZER", "google/flan-t5-base")

# Model generation constants
# Maximum user token input for generation
MAX_INPUT_TOKEN_LENGTH = 512
# Minimum user token input for generation
MIN_INPUT_TOKEN_LENGTH = 1
# Maximum length for Forge generation output
MAX_OUTPUT_TOKEN_LENGTH = 64
# Number of alternative sequences generated at each step
# More beams improve results, but increase computation
NUM_BEAMS = 2
# Scales logits before soft-max to control randomness
# Lower values (~0) make output more deterministic
TEMPERATURE = 0.9
# Limits generated tokens to top K probabilities
# Reduces chances of rare word predictions
TOP_K = 20
# Applies nucleus sampling, limiting token selection to a cumulative probability
# Creates a balance between randomness and determinism
TOP_P = 0.10
