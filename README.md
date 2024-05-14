# Awesome Discord Scraper

This repository contains a simple script to scrape data from a README.md file of a GitHub repository listing [awesome Discord communities](https://github.com/mhxion/awesome-discord-communities/blob/main/README.md#awesome-discord-communities-) and convert it into JSON format for easy importing into a database.

## Features

- Scrape Discord community data from a README.md file
- Convert the extracted data to a JSON file

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/awesome-discord-scraper.git
    cd awesome-discord-scraper
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the `README.md` file from the target repository in the same directory as `scrape.py`.

2. Run the script:
    ```bash
    python scrape.py
    ```

3. The script will generate a `communities.json` file in the `data/` directory with the extracted data.

## Example

```json
[
    {
        "name": "Code::Together",
        "invite_code": "ekgFE4s",
        "official": false,
        "homepage": "https://together.codes/",
        "git": "https://github.com/codedtogether",
        "notable_channels": [
            "looking-for-dev",
            "challenges",
            "python",
            "javascript",
            "c-family",
            "java",
            "html-css-web-js",
            "dotnet",
            "databases",
            "hosting"
        ],
        "language": ["English"]
    },
    ...
]
