# About the repository
I explore different machine learning techniques to solve the problem related to credit card fraud transactions. 
In each folder you will find a different appoach to classify the transactions. 
- The first folder contains an example with an Autoencoder
- The second folder a Multi-layer Perceptron (MLP)
- The third folder a comparison between Random Forest, Logistic Regression and FastBDT (stochastic-gradient boosted decision tree) on a toy data-set highly unbalanced

# Dataset
You can download the dataset that I have used for this project at: https://www.kaggle.com/mlg-ulb/creditcardfraud

"The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions." (source: description from the mentioned webpage)

### Data exploration
Here is a very brief visualization decription of the data-set. On the this plot below red crosses are fraud transactions and in bleu genuine transactions.

![timeseries](https://user-images.githubusercontent.com/36447056/39690478-910e10da-51da-11e8-86cc-45c9ed49eeeb.png)
