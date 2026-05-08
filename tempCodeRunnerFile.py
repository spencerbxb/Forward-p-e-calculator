import yfinance as yf

import evaluator.symbol as symbol
import evaluator.dcf as dcf

def main():
    sym:str = input("Please input a symbol: ").upper()

    ticker = symbol.get(sym)

    if ticker is None:
        print("Invalid symbol. Please input a correct symbol")
        main()
        return

    try:
        info = ticker.info

        market_cap = info.get("marketCap")
        beta = info.get("beta", 1.0)

        cashflow = ticker.cashflow

        # Get historical free cash flow values
        # yfinance labels may vary
        if "Free Cash Flow" not in cashflow.index:
            print("No free cash flow data available.")
            return

        fcf_series = cashflow.loc["Free Cash Flow"].dropna().tolist()

        if len(fcf_series) < 2:
            print("Not enough FCF history.")
            return

        # Estimate growth from historical FCF CAGR
        oldest = fcf_series[-1]
        newest = fcf_series[0]

        years = len(fcf_series) - 1

        fcf_growth_val = subdata.getFCFGrowth(t)

        intrinsic_value = dcf.calculate(
            fcf_series=fcf_series,
            growth=growth,
            beta=beta
        )

        print(f"\nSymbol: {sym}")
        print(f"Estimated growth: {growth:.2%}")
        print(f"Intrinsic enterprise value: ${intrinsic_value:,.0f}")

        if market_cap:
            ratio = market_cap / intrinsic_value

            print(f"Market cap: ${market_cap:,.0f}")
            print(f"Price / DCF ratio: {ratio:.2f}")

            if ratio < 1:
                print("Potentially undervalued.")
            else:
                print("Potentially overvalued.")

    except Exception as e:
        print("Error:", e)


main()