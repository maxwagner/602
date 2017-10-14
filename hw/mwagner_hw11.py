import pylab as py
import numpy as np
import pandas as pd
import random


apple = pd.read_csv('http://pastebin.com/raw/i9zkzPbf', names = ['date', 'price', 'delta'])
apple = apple.drop(0)
apple = apple.set_value(1, 'delta', 0)
apple.delta = pd.to_numeric(apple.delta)
last_price = float(apple.price[len(apple)-1])
delta_mean = float(np.mean(apple.delta))
delta_std = float(np.std(apple.delta))

prices = []
for i in range(10000):
    last_price_monte = last_price
    for i in range(20):
        rand = random.gauss(delta_mean, delta_std)
        last_price_monte = last_price_monte * (1 + rand)
    prices.append(last_price_monte)

one_percent = int(np.ceil(len(prices) * .01))
predict = sorted(prices)[one_percent - 1]
print ("After 20 days we can be 99 percent confident that stock price will be above %f dollars." % predict)