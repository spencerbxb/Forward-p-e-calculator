import evaluator.symbol as symbol
import evaluator.dcf as dcf
import evaluator.getinfo as getinfo
import evaluator.displayinfo as displayinfo

def main():
    sym:str = input("Please input a symbol: ").upper()

    # pull the ticker of the symbol
    ticker = symbol.fetch(sym)

    # if the ticker is nil, then symbol was likely incorrectly submitted
    if ticker is None:
        print(f"{sym} is not a valid symbol.")
        print(f"please ensure the symbol has been spelt correctly")
        print(f"or enter a valid symbol.")
        return

    try:
        # get the info from the symbol
        info = ticker.info

        # get significant data (market cap and beta)
        marketCap:float = info.get("marketCap")
        beta:float = info.get("beta", 1.0)

        # get the fcfSeries of the company
        fcfSeries = getinfo.getFCF(ticker, sym)
        if fcfSeries is None: return

        # get the average FCF of the company (from the past 3 years)
        avgFCF:float = getinfo.getAverageFCF(fcfSeries, sym)
        if avgFCF is None: return

        # get the growth information
        growth:float = getinfo.getGrowth(ticker, sym)
        if growth is None: return

        # use dcf calculation to derive an instrinic value
        intrinsicValue:float = dcf.calculate(avgFCF, growth, beta)

        # print info to the console
        displayinfo.printInfo(sym, avgFCF, growth, intrinsicValue, marketCap)

    except Exception as e:
        print("Error:", e)

main()