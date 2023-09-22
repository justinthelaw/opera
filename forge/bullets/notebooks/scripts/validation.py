import torch
import numpy as np
from rouge_score import rouge_scorer
from loguru import logger

from scripts.constants import *


# Function to evaluate model for predictions and compute ROUGE scores
def rouge_validation(tokenizer, model, loader):
    predictions = []
    actuals = []

    # Initialize the rouge scorer
    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
    scores = []

    with torch.no_grad():
        for _, data in enumerate(loader, 0):
            y = data["target_ids"].to(device, dtype=torch.long)
            ids = data["source_ids"].to(device, dtype=torch.long)
            mask = data["source_mask"].to(device, dtype=torch.long)

            generated_ids = model.generate(
                input_ids=ids,
                attention_mask=mask,
                max_length=max_input_token_length,
                num_beams=number_of_beams,
                repetition_penalty=repetition_penalty,
                length_penalty=length_penalty,
                early_stopping=True,
            )
            preds = [
                tokenizer.decode(
                    g, skip_special_tokens=True, clean_up_tokenization_spaces=True
                )
                for g in generated_ids
            ]
            targets = [
                tokenizer.decode(
                    t, skip_special_tokens=True, clean_up_tokenization_spaces=True
                )
                for t in y
            ]

            # Calculate rouge scores for each prediction and corresponding target
            for pred, target in zip(preds, targets):
                score = scorer.score(target, pred)
                scores.append(score)

            predictions.extend(preds)
            actuals.extend(targets)

    # Compute the average ROUGE scores for the entire validation set
    avg_scores = {
        "rouge1": np.mean([score["rouge1"].fmeasure for score in scores]),
        "rouge2": np.mean([score["rouge2"].fmeasure for score in scores]),
        "rougeL": np.mean([score["rougeL"].fmeasure for score in scores]),
    }

    logger.info(f"Average ROUGE scores: {avg_scores}")

    return predictions, actuals
