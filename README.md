# Data Ninja 

## Overview

This project is an intelligent web data extractor that fetches, parses, generates, and stores item data from web pages. It combines elements of web crawling, parsing, data generation, and database management to provide a comprehensive solution for extracting and enriching web data.

## Features

- **Fetching**: Retrieves web pages using proxies to avoid rate limits and blocks.
- **Parsing**: Extracts relevant item details from the HTML content.
- **Generating**: Uses GPT-4 to generate detailed item data based on the parsed details.
- **Storing**: Saves the extracted and generated data into a SQLite database.
- **Concurrency**: Handles multiple requests concurrently for efficiency.
- **Scheduling**: Automates periodic data extraction using a scheduler.
- **Configuration Management**: Manages settings and inputs through configuration files.

## Project Structure

1. `main.py` - Main entry point of the script.
2. `fetcher.py` - Handles fetching the item page.
3. `parser.py` - Parses the item details from the HTML content.
4. `generator.py` - Generates the item data using GPT-4.
5. `database.py` - Manages database operations.
6. `utils.py` - Contains utility functions, like loading proxies and configurations.
7. `scheduler.py` - Manages task scheduling.
8. `config.ini` - Configuration file.
9. `proxies.json` - Contains the list of proxies.
10. `items.json` - Contains the list of item URLs.
11. `.env` - Contains environment variables.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/data-ninja.git
   cd data-ninja
   ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env file and add your OpenAI API key:**

    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Configuration

### config.ini

    ```ini
    [DEFAULT]
    ProxiesFile = proxies.json
    ItemsFile = items.json
    MaxWorkers = 5
    Retries = 5
    BackoffFactor = 2
    ScheduleInterval = 1

    [DATABASE]
    DatabaseFile = items.db

    [API]
    OpenAIKey = your_openai_api_key_here
    ```

### proxies.json
* Contains the list of proxies.

    ```json
    {
        "proxies": [
            "http://your_proxy",
            "http://your_proxy"
        ]
    }
    ```

### items.json
Contains the list of item URLs.

    ```json
    {
    "item_urls": [
        "https://item_url",
        "https://another_item_url"
    ]
    }
    ```

