# OpenAI Audio Summarizer

Transcribes and summarizes a cut of an audio file with OpenAI APIs.

## Description

This is a simple script that takes a path to an audio file ([supported formats][https://platform.openai.com/docs/guides/speech-to-text]), takes a cut of it based on user provided start and end timestamps, uses the OpenAI Whisper API to transcribe the text and a GPT API to summarize it.

## Setup

To set up your environment to run the script, you'll need to install the Python requirements and get an API key.

### Python Dependencies

Install the Python dependencies by running: `pip install -r requirements.txt`

### OpenAI Key

To get an API key, sign up on the OpenAI website and follow their instructions. Once you have the API key, either create a file called `.env` at the top level of the local copy of this repository with a line `OPENAI_API_KEY=<your-key>` or set the key as an environmental variable at run time.

## Use

Modify the capitalized global variables (IN_PATH, SLICE_PATH, END_MINUTES, etc.) in `script.py` to your preferences.  

If you did not create the `.env` file in the setup, run `export OPENAI_API_KEY=<your-key>` before running the script.  

Run the script with: `python script.py`.  

The script will save the transcript and print the summary.
