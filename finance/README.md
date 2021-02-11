# About
This repository focuses on quantitative finance analysis.

# portfolio_measures
Exercise to calculate common technical fund informatino such as TE, beta, correlation and volatility.   
In the next update we will see how we can add the weight re-balancing in the logic.

Important reminder:
  1) Simple returns are additive in a portfolio but not log returns
  2) Simple returns are not additive over time
  3) Stock returns do NOT follow a normal distribution since in comparison they have fatter tails and are negatively skewed.
 
In the picture below, rp is the portfolio return in 2020 and ret_SP500 is our benchmark.  
The constitutens of the portfolio are the SPY, TLT and GLD.  

![téléchargement](https://user-images.githubusercontent.com/36447056/106645323-7b191400-658c-11eb-88fc-14d60e6742f9.png)


# call_option_pricing_example
Simple code to compute a call option price using the Monte-Carlo simulation in the BS framework.


# monte_carlo_simulations
The notebook shows a simple example of a Monte Carlo simulation using the Euler discretization scheme with a simple geometric browninan motion and in the second  
example with the Heston model.  
The main difference with the first example is that this time we allow the volatility to be stochastic and thus is more realistic for simulating e.g. stock prices.  

![téléchargement](https://user-images.githubusercontent.com/36447056/107699677-aef3e800-6cb6-11eb-9350-d5f76417f970.png)

