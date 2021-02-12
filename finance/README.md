# About
This repository focuses on quantitative finance analysis.

# portfolio_measures
Exercise to calculate common technical fund informatino such as TE, beta, correlation and volatility.   
Note: In the next update we will see how we can add the weight re-balancing in the logic.

Important reminder:
  1) Simple returns are additive in a portfolio but not log returns
  2) Simple returns are not additive over time
  3) Stock returns do NOT follow a normal distribution since in comparison they have fatter tails and are negatively skewed.
 
In the picture below, rp is the portfolio return in 2020 and ret_SP500 (S&P 500) is our benchmark.  
The constitutens of the portfolio are the SPY, TLT and GLD.  

![cumulative](https://user-images.githubusercontent.com/36447056/107700637-1199b380-6cb8-11eb-8a79-2804f520cfe0.png)


# call_option_pricing_example
Simple code to compute a call option price using the Monte-Carlo simulation in the BS framework.


# monte_carlo_simulations
The notebook shows two examples of a Monte Carlo simulation using the Euler discretization scheme. The first one  
is a simple geometric browninan motion and the second example uses the Heston model.  
The main difference with the first example is that this time we allow the volatility to be stochastic and thus is more realistic for simulating e.g. stock prices.  

![pgf_texsystem (2)](https://user-images.githubusercontent.com/36447056/107700396-b9fb4800-6cb7-11eb-8219-85ba4112b761.png)



