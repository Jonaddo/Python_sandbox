import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
style.use('ggplot')

M = 80    # Number of simulations
N = 10    # Number of days to simulate
S_t = np.zeros([N, M])
l_bound, u_bound = np.zeros([N, 1]), np.zeros([N, 1])
S_t[0, :], l_bound[0, 0], u_bound[0, 0] = 17, 17, 17
sigma = 0.37
mu = 0.017
dt = 1/10
Z_t = np.random.normal(0, dt, [N, M])

for i in range(N-1):
    for j in range(M):
        S_t[i+1, j] = S_t[i, j] + mu*S_t[i, j]*dt + sigma*S_t[i, j]*np.sqrt(dt)*Z_t[i, j]

drift = np.mean(S_t, axis=1)
for i in range(N - 1):
        l_bound[i+1, 0] = drift[i+1] - 1.96*sigma*np.sqrt(i+1)/np.sqrt(N)
        u_bound[i+1, 0] = drift[i+1] + 1.96*sigma*np.sqrt(i+1)/np.sqrt(N)

plt.figure(num=1)
plt.plot(S_t, '#808080')
plt.plot(drift, '-r', linewidth=2.0)
plt.plot(l_bound, '-k', linewidth=2.0)
plt.plot(u_bound, '-k', linewidth=2.0)
plt.xlabel('time')
plt.ylabel('Stock price')
plt.title('Monte Carlo simulation - Euler Scheme')
plt.show()
