#!/usr/bin/env bash
set -e  # Exit if any command fails

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
