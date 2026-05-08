import settings

# print(sym, avgFCF, growth, instrinicValue, marketCap) prints relevant data
# to the console for user lecture.
def printInfo(sym:str, avgFCF:float, growth:float, intrinsicValue:float, marketCap:float):
    print(f"\nSymbol: {sym}")
    print(f"Average FCF (3Y): ${avgFCF:,.0f}")
    print(f"Estimated growth: {growth:.2%}")
    print(f"Estimated intrinsic enterprise value: ${intrinsicValue:,.0f}")

    if marketCap and intrinsicValue > 0:
        ratio:float = marketCap / intrinsicValue

        print(f"Market cap: ${marketCap:,.0f}")
        print(f"Price / DCF ratio: {ratio:.2f}")

        if ratio < settings.OVERVALUED_THRESHOLD:
            print(f"Company {sym} is potentially undervalued.")
        elif ratio == settings.OVERVALUED_THRESHOLD:
            print(f"Company {sym} is fairly valued")
        else:
            print(f"Company {sym} is potentially overvalued.")
            
    else:
        print(f"Company {sym} has a negative intrinsic value")