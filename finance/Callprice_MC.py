import numpy as np

mu = 0
sigma = 0.17
delta_t = 1 / 260
rf = 0.0115
K = 130
D = 260


# Number of simulations
N = 1000

StockPrice = np.zeros((D, N))
eps = np.random.standard_normal((D, N))

for j in range(0, N - 1):
    for i in range(0, D - 1):
        StockPrice[0, j] = 126.54
        StockPrice[i + 1, j] = StockPrice[i, j] + StockPrice[i, j] * \
                                                  (mu * delta_t + sigma * eps[i, j] * np.sqrt(delta_t))

Payoff = np.zeros((N, 1))
for k in range(0, N - 1):
    if StockPrice[D - 1, k] > K:
        Payoff[k] = StockPrice[D - 1, k] - K
    else:
        Payoff[k] = 0

Payoff_mean = np.mean(Payoff)
Callprice = Payoff_mean / (1 + rf)

print(Callprice)

