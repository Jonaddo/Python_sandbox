import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

M = 80    # Number of simulations
N = 10    # Number of days to simulate
S_t = np.zeros([N, M])
S_t[0, :] = 17
sigma = 0.37
mu = 0.017
dt = 1/10
Z_t = np.random.normal(0, dt, [N, M])

for i in range(N-1):
    for j in range(M):
        S_t[i+1, j] = S_t[i, j] + mu*S_t[i, j]*dt + sigma*S_t[i, j]*np.sqrt(dt)*Z_t[i, j]

drift = np.mean(S_t, axis=1)
lower, upper = np.percentile(S_t, [2.5, 97.5], axis=1)

plt.figure(num=1)
plt.plot(S_t, '#808080')
plt.plot(drift, '-r', linewidth=2.0)
plt.plot(lower, '-k', linewidth=2.0)
plt.plot(upper, '-k', linewidth=2.0)
plt.xlabel('time')
plt.ylabel('Stock price')
plt.title('MC simulation - Black-Scholes model')
plt.show()
