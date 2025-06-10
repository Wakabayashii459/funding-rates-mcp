"""Example script to display funding rates for a few major tokens across all supported exchanges."""

from funding_rates_mcp.cli import compare_funding_rates, SUPPORTED_EXCHANGES


def main() -> None:
    symbols = ["BTC/USDT:USDT", "ETH/USDT:USDT"]
    result = compare_funding_rates(symbols=symbols, exchanges=SUPPORTED_EXCHANGES)
    print(result)


if __name__ == "__main__":
    main()
