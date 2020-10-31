import numpy as np
from sklearn import linear_model

#receive data points
data = input().split(" ")
m = float(data[0]) #money
k = int(data[1]) #available stocks
d = int(data[2]) #days left
predChange =[] #predicted increase or decrease
stocks=[]
stocktrans =[]
x = [1,2,3,4,5] #days of prices
def get_data(stock):
    prices=[]
    for i in range(2,7):
        prices.append(float(stock[i]))
    return prices

def predict_stock(x,prices,nextVal):
    linear_mod = linear_model.LinearRegression()
    x = np.reshape(x,(len(x),1))
    prices = np.reshape(prices,(len(prices),1))
    linear_mod.fit(x,prices)
    predicted_price =linear_mod.predict(x)
    return predicted_price[0][0],linear_mod.coef_[0][0] ,linear_mod.intercept_[0]

#sell all postive coefficients and buy all negatives
def transaction(changes):
    remaining = m
    for j in range(k):
        if changes[j] < -2.5 and remaining>0 and float(stocks[j][6]) < remaining:
            amountbought=(remaining // float(stocks[j][6]))
            stocktrans.append((stocks[j][0],"BUY",int(amountbought)))
            remaining-=(float(stocks[j][6])*amountbought) 
        else:
            if float(stocks[j][1]) > 0 and changes[j] > 1:
                stocktrans.append((stocks[j][0],"SELL",int(stocks[j][1])))
                 
    return 
for i in range(k):
    stocks.append(input().split(" "))

for stock in stocks:
    prices = get_data(stock)
    predicted_price, coefficient, constant = predict_stock(x,prices,6) 
    predChange.append(coefficient)
    #print("The predicted price is" + predicted_price)
#print(predChange)
transaction(predChange)

print(len(stocktrans))
for x in stocktrans:
    print(x[0],x[1],x[2])