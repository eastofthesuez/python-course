returns = [0.04, -0.02, 0.03, 0.01, -0.05, 0.06]

for r in returns:
    print(r)

total = 0
for r in returns:
    total = total + r
print(total)


def average(values):
    return sum(values)/ len(values)

def stdev(values):
    avg = average(values)
    total = 0
    for v in values:
        total = total + (v - avg)** 2
    variance = total / (len(values) - 1)
    return variance ** 0.5

print(stdev(returns))

def sharpe(values, periods_per_year, risk_free=0.0):
    excess = average(values) - risk_free/ periods_per_year
    return excess / stdev(values) * periods_per_year ** 0.5

print(sharpe(returns, 12))
print(sharpe(returns, 12, 0.04))

