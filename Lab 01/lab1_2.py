import pandas as pd 
import numpy as np 
import statistics as st
import matplotlib.pyplot as plt 

# Loading the CSV file into irctc variable
irctc = pd.read_excel("lab1.xlsx",sheet_name="IRCTC")
irctc = irctc.dropna(axis=1)
# print(irctc.head())

# Calculate the mean and variance of the Price data present in column D.
# (Suggestion: if you use Python, you may use statistics.mean() &
# statistics.variance() methods).

# First Select feature Price
# PRICE = irctc['Price'].dropna(axis=1)
M = st.mean(irctc["Price"])
Var = st.variance(irctc["Price"])
print("Mean of the data: ",M)
print("Variance        : ",Var)

#  Select the price data for all Wednesdays and calculate the sample mean. Compare the mean
#  with the population mean and note your observations.
Wed = irctc[irctc['Day']=='Wed']
# print(Wed.head())

Wed_mean = st.mean(Wed['Price'])
# print("Sample mean: ",Wed_mean)

# Comparing the sample mean with population mean
if Wed_mean < M:
    print("Mean of price data for all Wednesdays is lesser than the mean of all price")
else:
    print("Mean of price data for all Wednesdays is greater than the mean of all price")

# Select the price data for the month of Apr and calculate the sample mean. Compare the
# mean with the population mean and note your observations.
Apr_data = irctc[irctc['Month']=='Apr']
Apr_mean = st.mean(Apr_data['Price'])
print("Mean of price of April month: ",Apr_mean)

if Apr_mean < M:
    print("Population mean is greater than the sample mean of April month")
else:
    print("Population mean is greater than the sample mean of April month")
# From the Chg% (available in column I) find the probability of making a loss over the stock.
# (Suggestion: use lambda function to find negative values)

loss = irctc[irctc['Chg%']<0]

loss_pr = len(loss)/len(irctc)
print("Probability of loss over the stock price: ",loss_pr)

'''Calculate the probability of making a profit on Wednesday.'''
profit = irctc[irctc['Chg%']>0]
profit_wed = len(Wed)/len(profit) # Wed data we have calculated earlier
print("Probability of profit on Wednesday       : ",profit_wed)
'''Calculate the conditional probability of making profit, given that today is Wednesday.'''
Total_wed = len(Wed)

# Total_profit = len(profit)
profit_on_Wed = len(Wed['Chg%']>0)
Cnd_pr = profit_on_Wed/Total_wed
print("Conditional probability: ",Cnd_pr)

'''Make a scatter plot of Chg% data against the day of the week'''
X = irctc['Chg%']
Y = irctc['Day']
plt.scatter(X,Y,label='Data Points',color='blue')
plt.xlabel("Chg%")
plt.ylabel("Week")
plt.show()