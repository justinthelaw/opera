#!/bin/bash

# This bash script is used for fine-tuning the Bullet Forge model in
# Open AI's API - please refer to the README for more details

# Check if the OpenAI CLI tool is installed
if ! command -v openai &> /dev/null; then
  echo "==> OpenAI CLI is not installed!"
  exit 1
fi

# Check if the required arguments are provided
if [ $# -ne 2 ]; then
  echo "==> Usage: $0 <JSON_FILE> <BASE_MODEL>"
  exit 1
fi

# Assign the input arguments to variables
JSON_FILE=$1
BASE_MODEL=$2

# Prepare training data
echo "==> Preparing training data..."
PREPARED_DATA=$(openai tools fine_tunes.prepare_data -f "$JSON_FILE")
if [ $? -ne 0 ]; then
  echo "\r==> Failed to prepare training data. Exiting..."
  exit 1
fi
echo "==> Training data preparation completed!"

# # Start fine-tuning job
# echo "==> Starting fine-tuning job..."
# FINE_TUNED_MODEL=$(openai api fine_tunes.create -t "$PREPARED_DATA" -m "$BASE_MODEL")
# echo "==> Fine-tuning job started."

# # Wait for fine-tuning to complete
# echo "==> Waiting for fine-tuning to complete..."
# while true; do
#   JOB_STATUS=$(openai api fine_tunes.get -i "$FINE_TUNED_MODEL")
#   if [ "$JOB_STATUS" == "succeeded" ]; then
#     break
#   fi
#   sleep 10
# done
# echo "==> Fine-tuning completed!"

# # Instructions for using the fine-tuned model
# echo "==> Fine-tuned model usage: openai api completions.create -m '$FINE_TUNED_MODEL' -p <YOUR PROMPT>"
