strategy = {"name": "basis trade", "cagr": 0.12, "sharpe": 1.8, "max_dd": -0.06}

print(strategy)
print(strategy["sharpe"])

strategy["aum_musd"] = 25
strategy["sharpe"] = 1.7
print(strategy)

for key,value in strategy.items():
    print(key, value)

returns = {
       "basis": [0.01, 0.012, 0.008, 0.011],
       "options": [0.03, -0.02, 0.04, -0.01],
       "momentum": [0.05, -0.06, 0.02, 0.03]
   } 

for name, monthly in returns.items():
    total = 0
    for r in monthly:
        total = total + r
    average = total / len(monthly)
    print(name, round(average, 4))

def max_drawdown(values):
    nav = 1.0
    peak = 1.0
    worst = 0.0
    for r in values: 
        nav = nav * (1 + r)
        if nav > peak:
            peak = nav
        dd = (nav - peak) / peak
        if dd < worst:
            worst = dd
    return worst

example = [0.05, -0.03, -0.04, 0.02, 0.06, -0.01]
print(round(max_drawdown(example), 4))

for name, monthly in returns.items():
    print(name, round(max_drawdown(monthly), 4))


results ={}
for name, monthly in returns.items():
    results[name] = max_drawdown(monthly)
print(results)