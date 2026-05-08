def calculate(fcf0:float, growth:float, beta:float):

    # Discount rate
    r = 0.08 + (beta * 0.04)

    # Prevent invalid math
    if r <= 0.02:
        r = 0.03

    terminalGrowth = 0.02

    terminalValue = 0
    fcf_t = fcf0

    # 5-year forecast
    for t in range(1, 6):

        fcf_t *= (1 + growth)

        discounted = fcf_t / ((1 + r) ** t)

        terminalValue += discounted

    # Terminal value
    terminalValue = (
        fcf_t * (1 + terminalGrowth)
    ) / (r - terminalGrowth)

    terminalDiscounted = terminalValue / ((1 + r) ** 5)

    terminalValue += terminalDiscounted

    return terminalValue