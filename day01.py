returns = [0.04, -0.02, 0.03, 0.01, -0.05, 0.06]

print(len(returns))
print(sum(returns))
print(sum(returns) / len(returns))
print(returns[0])
print(returns[-1])

def average(values):
    return sum(values) / len(values)

print (average(returns))

def total_return(values):
    growth = 1.0
    for r in values: 
        growth = growth * (1 + r)
    return growth - 1

def cagr(values, periods_per_year):
    years = len(values) / periods_per_year
    return (1+ total_return(values)) ** (1 / years) -1

print(total_return(returns))
print(cagr(returns, 12))