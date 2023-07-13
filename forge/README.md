# Bullet Forge

Bullet Forge is Smarter Bullets' narrative generation tool that harnesses the power of Natural Language Processing (NLP) through distributed Hugging Face models. Bullet Forge is an API that is connected to a set of fine-tuned models that has been trained using 33,000+ unique EPR, OPR, and Award packages and bullets, across all of the Air and Space Force's positions and ranks.

The primary objective of this tool is to streamline the process of listing accomplishments and achievements by:

1. Offloading the cognitive and administrative burden of transforming factual information into effective Bullets
2. Offering suggestions to rephrase verbs, impacts, and outcomes to enhance variety and avoid repetition throughout the document
3. Intelligently incorporating acronyms to optimize spacing and enhance the readability of Bullets, while maintaining consistency across the document(s)

## Model Pulling

The usage of the models is within the Jupyter Notebooks contained within the [notebooks/](./notebooks/) directory and implementation of the models is within the Smarter Bullets [server/](../server/) directory.

To pull new copies of pre-trained models, first follow the instructions in [Virtual Environments](#virtual-environments), then execute the following:

```bash
# MODEL_NAME can be copied off of the hugging face repositories
python3 ./scripts/pull_model.py <MODEL_NAME>
```

## Fine Tuning

The Smarter Bullets fine-tuned models have been trained using 33,000+ unique EPR, OPR, and Award package bullets, across all Air and Space Force positions and ranks. A training, validation, and test data set are used to perform human-supervised training as well as manual and automatic inspection of model performance.

First, please follow the instructions in [Virtual Environments](#virtual-environments). To run your fine tuning, follow and use the [fine tuning Jupyter Notebook](./notebooks/fine_tune_training.ipynb).

### WandB

[Weights and Biases](https://wandb.ai/) was used to collect runs and metrics to optimize the fine tuning of the Bullet Forge models. In order to run the [fine tuning Jupyter Notebook](./notebooks/fine_tune_training.ipynb), the user will need to create a Weights and Biases account and login when prompted by a block within the Jupyter Notebook.

### Scraping

Some of the data was sourced from the contributors and the contributors' peers, but much more data was required to build the fine tuning data sets for Bullet Forge. Custom Python scripts were written to perform scraping on different bullet repositories that are publicly available. Some examples of websites with open-source bullets include:

-   http://www.eprbullets.com/
-   http://www.eprbulletsafsc.com/
-   http://www.airforcewriter.com/

First, please follow the instructions in [Virtual Environments](#virtual-environments).

To scrape, clean, and consolidate data, follow and use the [training data and model pulling Jupyter Notebook](./notebooks/prepare_data_model.ipynb). The data within [data/training/](./data/training/) is already prepared for fine tuning and should not need further modifications. Contributors are welcome to add more data from other websites beyond those identified within this repository.

### Contributing Bullets

Unclassified bullets can be added to [contributed.txt](./data/raw/contributed.txt) or through the toggling of the Smarter Bullets application's metrics collections permissions.

## Virtual Environments

A best practice for developing in Python is using a virtual environment (venv). Within README's this directory is a [requirements.txt](./requirements.txt) file for installing the dependencies required by `python3` to run the Jupyter Notebook contents.

To properly develop locally and contribute to Bullet Forge, please follow the contributing instructions in [repository README](../README.md), and also the following Bullet Forge development-specific instructions:

1. To create the venv, execute the following:

```bash
python3 -m venv .venv
```

2. To activate the venv, execute the following:

```bash
source /.venv/bin/activate
```

3. To install requirements into your venv, execute the following:

```bash
pip3 install -r forge/requirements.txt
```

4. To record any dependency changes, execute the following:

```bash
pip3 freeze > forge/requirements.txt
```

## Jupyter Notebooks

Please ensure all outputs and inputs you have provided to the Jupyter Notebooks are cleaned.
