# Stock Portfolio Performance Tracker 

A console-based stock portfolio tracking application built with Python 3. It allows users to enter stock tickers, purchase prices, share quantities, and current sample prices to calculate individual stock performance and overall portfolio returns. The results are saved to a CSV file for historical tracking.

##  Features

-  Tracks multiple stock holdings in one portfolio
-  Calculates invested capital and current market value
-  Calculates profit, loss, and percentage return
-  Displays individual stock performance and portfolio totals
-  Validates stock tickers against a provided dataset
-  Prevents duplicate stock tickers
-  Validates prices and share quantities
-  Saves portfolio summaries to a CSV file
-  Adds timestamps to recorded results
-  Supports CSV datasets with `Symbol` or `Ticker` columns
-  Uses the `Security` column for company names when available
-  Handles missing, empty, or unreadable datasets with clear error messages
-  Works offline without an internet connection
-  Uses only Python's standard library

##  Project Structure

```text
Stock-Portfolio-Tracker/
│
├── portfolio.py             # Main application
├── stock_tickers.csv        # Dataset of valid stock tickers
├── portfolio_summary.csv    # Generated portfolio history
└── README.md                # Project documentation
```

**Note:** `portfolio_summary.csv` is created automatically when the program saves its first portfolio report.

##  Requirements

- Python 3.x
- A stock ticker dataset named `stock_tickers.csv`
- No external Python packages required

The application uses Python's built-in modules:

`csv`, `os`, `datetime`, `zipfile`, and `xml.etree.ElementTree`

##  Installation and Setup

### 1. Install Python

Download Python 3 from the official website:

https://www.python.org/downloads/

### 2. Prepare the Project Files

Place `portfolio.py` and `stock_tickers.csv` in the same folder.

Ensure that the ticker dataset contains at least one supported column:

- `Symbol` — stock ticker symbols
- `Ticker` — an alternative ticker column

An optional `Security` column can contain company names.

### 3. Open a Terminal

Navigate to the project directory using Command Prompt or your preferred terminal.

### 4. Run the Application

Execute the following command:

```bash
python portfolio.py
```

On Windows, you can also use:

```bash
py portfolio.py
```

##  How to Use

1. Run the program.
2. The application loads the stock ticker dataset and displays example symbols.
3. Enter a valid stock ticker, such as `AAPL`.
4. Enter the purchase price per share.
5. Enter the number of shares purchased.
6. Enter the current sample price per share.
7. Repeat the process to add more holdings.
8. Type `DONE` when you have finished entering stocks.
9. Review the portfolio report displayed in the terminal.
10. Check `portfolio_summary.csv` for the saved results.

**Important:** Current stock prices are entered manually as sample values. The application does not fetch live market prices.

##  Calculations

The application calculates the following values for each holding and the overall portfolio.

| Metric | Formula |
|---|---|
| Invested Capital | Buy Price × Quantity |
| Market Value | Current Price × Quantity |
| Profit / Loss | Market Value − Invested Capital |
| Return (%) | (Profit / Loss ÷ Invested Capital) × 100 |
| Total Invested Capital | Sum of all holdings' invested capital |
| Total Market Value | Sum of all holdings' market values |
| Total Profit / Loss | Total Market Value − Total Invested Capital |
| Overall Return (%) | (Total Profit / Loss ÷ Total Invested Capital) × 100 |

All monetary values and percentage calculations are rounded to two decimal places in the saved summary.

##  Output File

The application records portfolio results in `portfolio_summary.csv`.

Each run appends new records instead of overwriting previous results, allowing users to maintain a history of portfolio calculations.

The file includes the following columns:

- `timestamp`
- `ticker`
- `company`
- `buy price`
- `quantity`
- `current price`
- `invested capital`
- `market value`
- `profit/loss`
- `profit/loss %`
- Portfolio total invested capital
- Portfolio total market value
- Portfolio total profit/loss
- Portfolio total return percentage

The exact column names depend on the implementation in `portfolio.py`.

##  Code Structure

| Function | Description |
|---|---|
| `load_stock_data()` | Loads valid stock tickers and company names from the dataset. |
| `get_positive_float()` | Accepts and validates positive numeric values for prices. |
| `get_positive_int()` | Accepts and validates positive whole numbers for share quantities. |
| `collect_portfolio()` | Collects stock holdings and stores them in a dictionary. |
| `calculate_performance()` | Calculates individual holding performance and portfolio totals. |
| `display_report()` | Prints the portfolio report and summary totals. |
| `save_summary()` | Appends portfolio results to `portfolio_summary.csv`. |
| `main()` | Runs the application and handles errors. |

##  Input Validation and Error Handling

The application includes validation to improve reliability:

- Stock tickers must exist in the provided dataset.
- Duplicate tickers are rejected.
- Purchase prices and current sample prices must be finite numbers greater than zero.
- Share quantities must be positive whole numbers.
- Missing, empty, or unreadable datasets produce clear error messages.
- If no holdings are entered, the program does not generate a portfolio report.

The dataset loader also supports several text encodings and handles an Excel `.xlsx` file saved with a `.csv` extension, according to the program's implementation.

##  Learning Objectives

This project demonstrates practical Python programming concepts, including:

- Functions and modular programming
- Dictionaries and data structures
- User input validation
- CSV file reading and writing
- Financial calculations
- Date and timestamp handling
- Exception handling and error management
- Data persistence through file storage

