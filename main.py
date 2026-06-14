import evaluator.symbol as symbol
import evaluator.displayinfo as displayinfo

def main():
    while True:
        sym:str = input("Please input a symbol, or enter 'EXIT' to quit: ").upper()

        if "EXIT" == sym:
            return

        # pull the ticker of the symbol
        ticker = symbol.fetch(sym)

        # if the ticker is nil, then symbol was likely incorrectly submitted
        if ticker is None:
            displayinfo.invalidSymbol(sym)
            return
        
        evaluateStock(sym, ticker)

def evaluateStock(sym:str, ticker:list):
    try:
        # get the forward p/e of the company
        forwardPE:float = ticker.info.get("forwardPE")

        # get the pe ttm:
        trailingPE:float = ticker.info.get("trailingPE")

        # get the growth estimates
        growthEstimates:float = ticker.info.get("earningsGrowth")

        # print info to the console
        displayinfo.printInfo(sym, forwardPE, trailingPE, growthEstimates)

    except Exception as e:
        print("Error:", e)

main()