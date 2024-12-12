# StockAnalyzer

StockAnalyzer is a Python-based tool designed to evaluate and analyze stock performance. It fetches stock data, popularity metrics, industry growth rates, and Shikiho data to provide a comprehensive evaluation of a stock's potential.

## Features

- **Stock Data Retrieval**: Fetches basic stock information such as name, sector, and current price using Yahoo Finance.
- **Popularity Metrics**: Retrieves the popularity of a company based on its name.
- **Industry Growth Rate**: Obtains the growth rate of the industry to which the company belongs.
- **Shikiho Data**: Scrapes and retrieves detailed financial data from Shikiho.
- **Stock Evaluation**: Evaluates the stock based on various metrics and assigns a score and rank.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/StockAnalyzer.git
    cd StockAnalyzer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. Enter the ticker symbol when prompted (e.g., `ED`).

## Example

```sh
Please enter the ticker symbol (e.g., ED): ED

Retrieved data:
name: Consolidated Edison Inc.
sector: Utilities
price: 75.23

Popularity: 45

Industry (Utilities) growth rate: 3%

Shikiho data:
growth: 12
profit_margin: 6

Evaluation result:
Score: 60
Rank: B
Details:
 - Moderate popularity (Score +10)
 - Industry is stable (Score +10)
 - High growth rate (Score +20)
 - High profit margin (Score +10)