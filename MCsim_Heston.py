import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Parameters
M = 50    # Number of simulations
N = 10    # Number of days to simulate
dt = 1/10
sigma = 0.37
mu = 0.017
kappa = 0.9
theta = 0.25
rho = -0.8  # negatively correlated since in bear markets volatility tends to be higher than in bull markets
S0 = 17

S_t = np.zeros([N, M])
v_t = np.zeros([N, M])
Z_t = np.random.normal(0, dt, [N, M])
Z2 = np.random.normal(0, dt, [N, M])
Z2_t = rho*Z_t + np.sqrt(1-rho**2)*Z2

S_t[0, :] = S0
v_t[0, :] = 0.22

for i in range(N-1):
    for j in range(M):
        S_t[i+1, j] = S_t[i, j] + mu*S_t[i, j]*dt + sigma*S_t[i, j]*np.sqrt(dt)*Z_t[i, j]
        v_t[i+1, j] = v_t[i, j] + kappa*(theta - v_t[i, j])*dt + sigma*np.sqrt(v_t[i, j]*dt)*Z2_t[i, j]

drift = np.mean(S_t, axis=1)
lower, upper = np.percentile(S_t, [2.5, 97.5], axis=1)
lower = np.percentile()
plt.plot(S_t, '#808080')
plt.plot(drift, '-r', linewidth=2.0)
plt.plot(lower, '-k', linewidth=2.0)
plt.plot(upper, '-k', linewidth=2.0)
plt.xlabel('time')
plt.ylabel('Stock price')
plt.title('MC simulation - Heston model')
plt.show()
