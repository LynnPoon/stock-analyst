#!/usr/bin/env python
import re
import sys
import warnings

from dotenv import load_dotenv

from stock_analyst.crew import StockAnalyst

load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def get_valid_ticker(prompt="Enter a stock code: "):
    """
    Prompts the user for a stock ticker and validates it.
    Supports global symbols (1-10 characters, including letters, numbers, dots, and hyphens).
    """
    while True:
        ticker = input(prompt).strip().upper()
        if re.match(r"^[A-Z0-9.\-]{1,10}$", ticker):
            return ticker
        print(
            "Invalid ticker format. Please enter 1-10 characters (e.g., AAPL, BP.L, 0700.HK)."
        )


def run():
    """
    Run the crew.
    """
    ticker = get_valid_ticker()
    inputs = {
        "ticker": ticker,
    }

    try:
        StockAnalyst().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    ticker = get_valid_ticker("Enter the stock ticker you want to train on: ")
    inputs = {
        "ticker": ticker,
    }
    try:
        StockAnalyst().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        StockAnalyst().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    ticker = get_valid_ticker("Enter the stock ticker you want to test: ")
    inputs = {
        "ticker": ticker,
    }

    try:
        StockAnalyst().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
