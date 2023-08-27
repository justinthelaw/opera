# The Forge

The primary objective of this tool is to streamline the process of listing accomplishments and achievements by:

1. Offloading the cognitive and administrative burden of transforming factual information into effective statements
2. Offering suggestions to rephrase verbs, impacts, and outcomes to enhance variety and avoid repetition throughout the document
3. Intelligently incorporating acronyms to optimize spacing and enhance the readability of Bullets, while maintaining consistency across the document(s)

## Directory Structure

There are two sub-directories that contain different scripts and training processes for each type of statements. One is focused on [Bullets](./bullets) and Bullet creation, while the other is focused on [Narratives](./narratives/) and Narrative creation.

The [Resources](./resources/) directory contains the PDF forms and other guidance for how statements should be written.

## Model Pulling

The usage of the models is within the Jupyter Notebooks contained within the _notebooks/_ directories. Models for Opera's Forge are not uploaded to this repository due to size, and will be made available via a future Hugging Face checkpoint or as a separately hosted archive.

**_IMPORTANT NOTE_**: The [.env.example](../config/.env.example) contains a placeholder model for both the Narrative and Bullet versions of Opera's Forge in order to pass the acceptance and server tests within the pipeline. Only change the local model within your own _.env.local_, which is created during the execution of `npm run install:all`.

To pull models specific to the ones trained for Opera's Forge please go to the following Hugging Face repositories:

1. [opera-bullet-interpreter](https://huggingface.co/justinthelaw/opera-bullet-interpreter)
2. [opera-bullet-forge-summarization](#)
3. [opera-bullet-forge-generator](#)
4. [opera-narrative-forge-summarization](#)
5. [opera-narrative-forge-generator](#)
6. [opera-narrative-interpreter](#)

## Fine Tuning

The Opera fine-tuned models have been trained using 33,000+ unique EPR, OPR, and Award packages, across all Air and Space Force positions and ranks. A training, validation, and test data set are used to perform human-supervised training as well as manual and inspection of model performance through ROGUE score.

First, please follow the instructions in [Virtual Environments](#virtual-environments). To run your fine tuning, follow and use the fine tuning Jupyter Notebooks located within the directories.

### Scraping

Some of the data was sourced from the contributors and the contributors' peers, but much more data was required to build the fine tuning data sets for The Forge. Custom Python scripts were written to perform scraping on different statement repositories that are publicly available. Some examples of websites with open-source bullets include:

- http://www.eprbullets.com/
- http://www.eprbulletsafsc.com/
- http://www.airforcewriter.com/

First, please follow the instructions in [Virtual Environments](#virtual-environments).

To scrape, clean, and consolidate data, follow and use the training data and model pulling Jupyter Notebooks located within the directories. The data within each directory's _data/training/_ is already prepared for fine tuning and should not need further modifications. Contributors are welcome to add more data from other websites beyond those identified within this repository.

### Contributing Statements

Unclassified statements can be added to _contributed.txt_ files in each directory's _data/raw/_ directories.

## Virtual Environments

A best practice for developing in Python is using a Virtual Environment (venv). Within this README's directory is a [requirements.txt](./requirements.txt) file for installing the dependencies required by `python3` to run the Jupyter Notebook contents.

To properly develop locally and contribute to The Forge, please follow the contributing instructions in [repository README](../README.md).

## Jupyter Notebooks

Please ensure all outputs and inputs you have provided to the Jupyter Notebooks are cleaned.
