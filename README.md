# Gemini API Python Examples

This repository contains two Python scripts demonstrating how to interact with the Google Gemini API.

## `gemi101.py`

This script provides a basic example of using the Gemini API to generate text. It initializes the Gemini client with an API key and then sends a simple query ("Explain how AI works") to the `gemini-2.5-flash` model, printing the response.

### Usage

1.  **Install the Google GenAI SDK:**
    ```bash
    pip install -q -U google-genai
    ```
2.  **Set your API Key:**
    Replace `API_KEY = ""` with your actual Gemini API key. You can obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).
    Alternatively, set the `GEMINI_API_KEY` environment variable.
3.  **Run the script:**
    ```bash
    python gemi101.py
    ```

## `gemi102.py`

This script implements a simple interactive coding helper chatbot using the Gemini API. It acts as an expert Python programmer, providing clear, concise, and accurate answers to user questions. If a code error is detected, it explains the error and provides corrected code.

### Usage

1.  **Install the Google GenAI SDK:**
    ```bash
    pip install -q -U google-genai
    ```
2.  **Set your API Key:**
    Replace `API_KEY = ""` with your actual Gemini API key. You can obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).
    Alternatively, set the `GEMINI_API_KEY` environment variable.
3.  **Run the script:**
    ```bash
    python gemi102.py
    ```
    You can then type your Python-related questions into the console. Type "quit" to exit the chatbot.

## Gemini API Quickstart Documentation

For more detailed information on setting up and using the Gemini API, refer to the official quickstart guide: [https://ai.google.dev/gemini-api/docs/quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
