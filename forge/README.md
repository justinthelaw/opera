# Bullet Forge

Bullet Forge is Smarter Bullets' narrative generation tool that harnesses the power of Natural Language Processing (NLP) through the use of the Text-To-Text Transfer Transformer (T5) base model. Bullet Forge is an API that is connected to a fine-tuned T5 model that has been trained using 33,000+ unique EPR, OPR, and Award packages and bullets, across all of the Air and Space Force's positions and ranks.

The primary objective of this tool is to streamline the process of listing accomplishments and achievements by:

1. Offloading the cognitive and administrative burden of transforming factual information into effective Bullets
2. Offering suggestions to rephrase verbs, impacts, and outcomes to enhance variety and avoid repetition throughout the document
3. Intelligently incorporating acronyms to optimize spacing and enhance the readability of Bullets, while maintaining consistency across the document(s)

## T5 Model

The usage of the T5 model is documented on the [T5 Hugging Face page](https://huggingface.co/docs/transformers/model_doc/t5) and within the Smarter Bullets `server/` and `forge/` code.

To pull a new copy of the T5 base model, first follow the instructions in [Virtual Environments](#virtual-environments), then execute the following:

```bash
python3 ./scripts/pull_model.py
```

## Fine Tuning

The Smarter Bullets fine-tuned T5 model has been trained using 33,000+ unique EPR, OPR, and Award package bullets, across all Air and Space Force positions and ranks, with semantically randomized initial inputs.

First, please follow the instructions in [Virtual Environments](#virtual-environments). To run your fine-tuning, follow and use the [fine tuning Jupyter Notebook](./notebooks/fine_tune.ipynb).

## Scraping

Some of the test data was sourced from the contributors and the contributors' peers, but much more data was required to build the fine-tuning data sets for Bullet Forge. Custom Python scripts were written to perform scraping on different bullet repositories that are publicly available. Some examples of websites with open-source bullets include:

-   http://www.eprbullets.com/
-   http://www.eprbulletsafsc.com/
-   http://www.airforcewriter.com/

First, please follow the instructions in [Virtual Environments](#virtual-environments).

To scrape, clean, and consolidate data, follow and use the [training data Jupyter Notebook](./notebooks/training_data.ipynb). The data within `data/training` is already prepared for fine-tuning and should not need further modifications. Contributors are welcome to add more data from other websites beyond those identified within the Jupyter Notebook.

## Virtual Environments

A best practice for developing in Python is using a virtual environment (venv). Within the root of this directory is a `requirements.txt` file for installing the dependencies required by `python3` to run the Jupyter Notebook contents.

To properly develop locally and contribute to Bullet Forge, please follow the [repository README](../README.md), and the following Bullet Forge development-specific instructions:

1. To create the venv, execute the following:

```bash
python3 -m venv .venv
```

2. To activate the venv, execute the following:

```bash
# Windows-based OS
\.venv\Scripts\activate
```

```bash
# MacOS or UNIX-based OS
source /.venv/bin/activate
```

3. To install requirements into your venv, execute the following:

```bash
pip install -r requirements.txt
```

4. To record any dependency changes, execute the following:

```bash
pip freeze > forge/requirements.txt
```

## Jupyter Notebooks

Please ensure all outputs and inputs you have provided to the Jupyter Notebooks are cleaned.
