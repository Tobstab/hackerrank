stock=[]
transdata =[]
buydata=[]
selldata=[]
data =input().split(" ")
m=int(data[0])
k=int(data[1])
d=int(data[2])
#print(m, k,d)

def transaction(transdata):
    for stock in transdata:
        if stock[2]>1:
            #buy
            buydata.append((stock[0],float(stock[3]),0))
        else:
            #sell stock greater than 0
            if stock[1] >0:
                selldata.append((stock[0],stock[1]))  
    sortedBuy = sorted(buydata, key=lambda buydata: buydata[1])  
    buy(sortedBuy,m)
    #new count for how many to purchase
    #count for non purchaseable stocks
def buy(sortedBuy,money):
    nopurch =0
    while money > 0:
        for purchase in sortedBuy:
            if purchase[1]<m:
                money-=purchase[1]
                lists=list(purchase)
                lists[2]+=1
                tuple(lists)
                purchase =lists
            else:
                nopurch+=1
        if nopurch == len(sortedBuy):
            print("0")
            break
    for purchase in sortedBuy:
        print(purchase)
        if purchase[2]>0:
            print(purchase[0], "BUY", purchase[2])
    for purchase in selldata:
        print(purchase)
    
                
    
for i in range(k):
    stock.append(input().split(" "))
#print(stock)
maxcount=0
for stkinfo in stock:
    count=0
    for i in range(2,6):
        if stkinfo[i+1]<stkinfo[i]:
            count+=1
        else:
            count=0
    transdata.append((stkinfo[0],int(stkinfo[1]),count,stkinfo[6]))
#print(transdata)
transaction(transdata)
