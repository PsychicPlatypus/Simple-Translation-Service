# Simple Translations Service

This is a simple translation service that uses the Argos Translate to translate text from one language to English.

## Requirements

- Python 3.10 or higher
- Optionally pipenv, but you can use any other virtual environment manager

## Installation

1. Clone the repository
2. Install the dependencies

    Using pipenv

    ```bash
    pipenv shell
    pipenv install
    ```

    Using pip

    ```bash
    python -m venv .venv # Or python3 -m venv .venv, depending on your system
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the server

    ```bash
    uvicorn translation.server:app --reload
    ```

4. Open your browser and go to `http://http://127.0.0.1:8000/docs#/` for the Swagger documentation

## Usage

Available language codes are:

|Code|Language|
| ---- | -------- |
|sq|Albanian|
|ar|Arabic|
|az|Azerbaijani|
|bn|Bengali|
|bg|Bulgarian|
|ca|Catalan|
|zh|Chinese|
|zt|Chinese (traditional)|
|cs|Czech|
|da|Danish|
|nl|Dutch|
|eo|Esperanto|
|et|Estonian|
|fi|Finnish|
|fr|French|
|de|German|
|el|Greek|
|he|Hebrew|
|hi|Hindi|
|hu|Hungarian|
|id|Indonesian|
|ga|Irish|
|it|Italian|
|ja|Japanese|
|ko|Korean|
|lv|Latvian|
|lt|Lithuanian|
|ms|Malay|
|nb|Norwegian|
|fa|Persian|
|pl|Polish|
|pt|Portuguese|
|ro|Romanian|
|ru|Russian|
|sk|Slovak|
|sl|Slovenian|
|es|Spanish|
|sv|Swedish|
|tl|Tagalog|
|th|Thai|
|tr|Turkish|
|uk|Ukranian|
|ur|Urdu|

It only translates to english, so the target language is not needed.
