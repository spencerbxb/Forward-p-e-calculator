# print(sym, avgFCF, growth, instrinicValue, marketCap) prints relevant data
# to the console for user lecture.
def printInfo(sym:str, forwardPE:float, trailingPE:float, growthEstimates:float):
    print(f"\nSymbol: {sym}")
    print(f"forward pe is: ${forwardPE:,.2f}")
    print(f"trailing pe is: ${trailingPE:,.2f}")
    if growthEstimates is None:
        print("growth estimates unavailable")
    else:
        print(f"growth estimates are: {growthEstimates * 100:.2f}%")

def invalidSymbol(sym:str):
    print(f"{sym} is not a valid symbol.")
    print(f"please ensure the symbol has been spelt correctly")
    print(f"or enter a valid symbol.")