import settings

# growth(info, sym) returns the growth estimate of a stock as a float,
# returns nothing if no estimate is available
def getGrowth(ticker, sym:str) -> float:
    # Use analyst growth estimate if available
    growth_df = ticker.growth_estimates

    # fallback if missing
    if growth_df is None:
        print(f"Growth not found for company {sym}")
        return
    
    fcf_growth = growth_df.loc["+1y"]["stockTrend"]
    
    return fcf_growth

def getFCF(ticker, sym:str):
    cashflow:float = ticker.cashflow

    # Verify FCF exists
    if "Free Cash Flow" not in cashflow.index:
        print("No free cash flow data available.")
        return

    # Get FCF history
    fcfSeries = cashflow.loc["Free Cash Flow"].dropna().tolist()

    if len(fcfSeries) < settings.REQUIRED_FCF_LENGTH:
        print(f"User defined {settings.REQUIRED_FCF_LENGTH} years of FCF data.")
        print(f"{sym} only has {len(fcfSeries)} years of data available")
        return
    
    return fcfSeries

def getAverageFCF(fcfSeries, sym:str):
    # get the latest free cash flow information
    recentFCF:float = fcfSeries[:settings.REQUIRED_FCF_LENGTH]

    avgFCF:float = sum(recentFCF) / len(recentFCF)

    # Reject invalid companies
    if avgFCF <= 0:
        print(f"Company {sym} has negative average FCF.")
        return
    
    return avgFCF