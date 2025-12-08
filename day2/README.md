# Hackathon Pitch Idea Generator

This project is a Python script that leverages the Google Gemini AI to generate innovative hackathon pitch ideas. 

## Project Overview

The script focuses on generating a detailed hackathon pitch, including:
- A catchy project name.
- A clear definition of the problem.
- A proposed solution utilizing relevant technologies.
- Key features of the solution.
- A concise "TLDR" summary of the idea.

The current theme is "Taking Humans to Mars," and the AI uses pre-defined web search context about Mars colonization technology to inform its pitch generation.

## Model

- **Google Generative AI (`google-generativeai`)**: Gemini AI model (`gemini-2.5-flash`).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/prajwal-56/muLearn-Bootcamp.git
    cd muLearn-Bootcamp
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your Google API Key:**
    *   Create a `.env` file in the root directory of the project.
    *   Add your Google API Key to this file in the following format:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
    *   You can obtain a Google API Key from the [Google AI Studio](https://aistudio.google.com/).

## How to Run

Execute the `main.py` script:

```bash
python main.py
```

The script will then print the generated hackathon pitch idea to your console.

## Customization

You can modify the `hackathon_theme` and `web_search_context` variables within `main.py` to generate pitches for different themes and contexts.
