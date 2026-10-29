
import csv
import os
from datetime import datetime
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "stock_tickers.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "portfolio_summary.csv")

SUMMARY_FIELDS = [
    "timestamp",
    "ticker",
    "company",
    "buy_price",
    "quantity",
    "current_price",
    "invested_capital",
    "market_value",
    "profit_loss",
    "profit_loss_percent",
    "portfolio_invested_total",
    "portfolio_market_total",
    "portfolio_profit_loss_total",
    "portfolio_return_percent",
]


def load_stock_data():

    if not os.path.isfile(DATA_FILE):
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )
    with open(DATA_FILE, "rb") as file:
        signature = file.read(4)

    rows = []

    if signature[:2] == b"PK":
        with zipfile.ZipFile(DATA_FILE, "r") as workbook:

            namespace = {
                "m": "http://schemas.openxmlformats.org/"
                     "spreadsheetml/2006/main",
                "r": "http://schemas.openxmlformats.org/"
                     "officeDocument/2006/relationships",
                "rel": "http://schemas.openxmlformats.org/"
                       "package/2006/relationships",
            }

            shared_strings = []

            if "xl/sharedStrings.xml" in workbook.namelist():
                root = ET.fromstring(
                    workbook.read("xl/sharedStrings.xml")
                )

                for item in root.findall("m:si", namespace):
                    shared_strings.append(
                        "".join(
                            node.text or ""
                            for node in item.findall(".//m:t", namespace)
                        )
                    )

            # Find the first worksheet in the workbook.
            workbook_root = ET.fromstring(
                workbook.read("xl/workbook.xml")
            )
            sheet = workbook_root.find(
                "m:sheets/m:sheet", namespace
            )

            if sheet is None:
                raise ValueError("No worksheet found in Excel file.")

            relationship_id = sheet.attrib.get(
                "{http://schemas.openxmlformats.org/"
                "officeDocument/2006/relationships}id"
            )

            relationships = ET.fromstring(
                workbook.read("xl/_rels/workbook.xml.rels")
            )

            target = None
            for rel in relationships.findall("rel:Relationship", namespace):
                if rel.attrib.get("Id") == relationship_id:
                    target = rel.attrib.get("Target")
                    break

            if not target:
                raise ValueError("Could not locate the worksheet.")

            if target.startswith("/"):
                sheet_path = target.lstrip("/")
            elif target.startswith("xl/"):
                sheet_path = target
            else:
                sheet_path = "xl/" + target

            sheet_root = ET.fromstring(
                workbook.read(sheet_path)
            )

            for row in sheet_root.findall(".//m:sheetData/m:row", namespace):
                values = []

                for cell in row.findall("m:c", namespace):
                    reference = cell.attrib.get("r", "")
                    column_letters = "".join(
                        char for char in reference if char.isalpha()
                    )

                    column_number = 0
                    for char in column_letters.upper():
                        column_number = (
                            column_number * 26
                            + ord(char) - ord("A") + 1
                        )

                    while len(values) < column_number:
                        values.append("")

                    cell_type = cell.attrib.get("t")
                    value_node = cell.find("m:v", namespace)

                    if cell_type == "inlineStr":
                        text_node = cell.find("m:is", namespace)
                        value = (
                            "".join(
                                node.text or ""
                                for node in text_node.findall(".//m:t", namespace)
                            )
                            if text_node is not None else ""
                        )
                    elif value_node is None:
                        value = ""
                    else:
                        value = value_node.text or ""

                        if cell_type == "s":
                            value = shared_strings[int(value)]

                    values[column_number - 1] = value

                rows.append(values)

    else:
        last_error = None

        for encoding in ("utf-8-sig", "cp1252", "latin-1"):
            try:
                with open(
                    DATA_FILE, "r", newline="", encoding=encoding
                ) as file:
                    rows = list(csv.reader(file))
                break
            except UnicodeDecodeError as error:
                last_error = error
        else:
            raise ValueError(
                f"Could not decode CSV file: {last_error}"
            )

        if rows and len(rows[0]) == 1 and "," in rows[0][0]:
            rows = list(csv.reader(row[0] for row in rows))

    if not rows:
        raise ValueError("Dataset is empty.")

    headers = [
        str(value).strip().lower()
        for value in rows[0]
    ]

    ticker_column = next(
        (
            headers.index(name)
            for name in ("symbol", "ticker", "ticker symbol")
            if name in headers
        ),
        None,
    )

    if ticker_column is None:
        raise ValueError(
            "Ticker column not found. Available columns: "
            + ", ".join(headers)
        )

    company_column = (
        headers.index("security")
        if "security" in headers
        else None
    )

    stocks = {}

    for row in rows[1:]:
        if len(row) <= ticker_column:
            continue

        ticker = str(row[ticker_column]).strip().upper()

        if not ticker:
            continue

        company = (
            str(row[company_column]).strip()
            if company_column is not None
            and len(row) > company_column
            else ticker
        )

        stocks[ticker] = company

    if not stocks:
        raise ValueError("No stock symbols found in the dataset.")

    print(f"Dataset loaded successfully: {len(stocks)} stock symbols.")
    return stocks


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())

            if value > 0 and value != float("inf") and value == value:
                return value

            print("Enter a finite number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a valid number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())

            if value > 0:
                return value

            print("Quantity must be greater than zero.")
        except ValueError:
            print("Enter a whole number, such as 10.")


def collect_portfolio(stocks):
    portfolio = {}

    print(f"\nLoaded {len(stocks)} stock symbols from the dataset.")
    print("Examples:", ", ".join(list(stocks.keys())[:10]))
    print("Type DONE to finish entering holdings.")

    while True:
        ticker = input("\nEnter stock ticker: ").strip().upper()

        if ticker == "DONE":
            break

        if not ticker:
            print("Ticker cannot be empty.")
            continue

        if ticker not in stocks:
            print("Ticker not found in the dataset.")
            continue

        if ticker in portfolio:
            print("Ticker already added. Enter it only once.")
            continue

        print(f"Company: {stocks[ticker]}")

        buy_price = get_positive_float("Enter buy price per share: ")
        quantity = get_positive_int("Enter number of shares: ")

        current_price = get_positive_float(
            "Enter current/sample price per share: "
        )

        portfolio[ticker] = {
            "company": stocks[ticker],
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price,
        }

        print(f"{ticker} added successfully.")

    return portfolio


def calculate_performance(portfolio):
    results = []
    total_invested = 0.0
    total_market_value = 0.0

    for ticker, item in portfolio.items():
        invested = item["buy_price"] * item["quantity"]
        market_value = item["current_price"] * item["quantity"]
        profit_loss = market_value - invested
        percentage = (profit_loss / invested) * 100

        results.append({
            "ticker": ticker,
            "company": item["company"],
            "buy_price": item["buy_price"],
            "quantity": item["quantity"],
            "current_price": item["current_price"],
            "invested_capital": invested,
            "market_value": market_value,
            "profit_loss": profit_loss,
            "profit_loss_percent": percentage,
        })

        total_invested += invested
        total_market_value += market_value

    total_profit_loss = total_market_value - total_invested
    overall_return = (
        total_profit_loss / total_invested * 100
        if total_invested else 0.0
    )

    totals = {
        "portfolio_invested_total": total_invested,
        "portfolio_market_total": total_market_value,
        "portfolio_profit_loss_total": total_profit_loss,
        "portfolio_return_percent": overall_return,
    }

    return results, totals


def display_report(results, totals):
    print("\n" + "=" * 100)
    print("          STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 100)

    print(
        f"{'Ticker':<9}{'Buy Price':>12}{'Shares':>9}"
        f"{'Current':>12}{'Invested':>14}{'Market Value':>15}"
        f"{'Profit/Loss':>14}{'Return %':>11}"
    )
    print("-" * 96)

    for row in results:
        print(
            f"{row['ticker']:<9}"
            f"{row['buy_price']:>12.2f}"
            f"{row['quantity']:>9}"
            f"{row['current_price']:>12.2f}"
            f"{row['invested_capital']:>14.2f}"
            f"{row['market_value']:>15.2f}"
            f"{row['profit_loss']:>14.2f}"
            f"{row['profit_loss_percent']:>10.2f}%"
        )

    print("-" * 96)
    print(f"Total invested: {totals['portfolio_invested_total']:.2f}")
    print(f"Market value:   {totals['portfolio_market_total']:.2f}")
    print(f"Total P/L:      {totals['portfolio_profit_loss_total']:.2f}")
    print(f"Overall return: {totals['portfolio_return_percent']:.2f}%")
    print("=" * 100)


def save_summary(results, totals):
    file_exists = (
        os.path.exists(OUTPUT_FILE)
        and os.path.getsize(OUTPUT_FILE) > 0
    )

    timestamp = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=SUMMARY_FIELDS)

        if not file_exists:
            writer.writeheader()

        for result in results:
            row = {
                "timestamp": timestamp,
                **result,
                **totals,
            }

            writer.writerow({
                key: round(value, 2) if isinstance(value, float) else value
                for key, value in row.items()
            })

    print(f"\nReport saved successfully: {OUTPUT_FILE}")


def main():
    print("Welcome to Stock Portfolio Performance Tracker!")

    try:
        stocks = load_stock_data()
        portfolio = collect_portfolio(stocks)

        if not portfolio:
            print("No holdings entered. No report generated.")
            return

        results, totals = calculate_performance(portfolio)
        display_report(results, totals)
        save_summary(results, totals)

    except (OSError, ValueError, csv.Error) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
