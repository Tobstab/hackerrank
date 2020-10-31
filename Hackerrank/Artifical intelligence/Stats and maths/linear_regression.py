import math

data =input().split(" ")
f= int(data[0])
n= int(data[1])

x =[]
y =[]
def get_data():
    for i in range(n):
        features = input().split(" ")
        x.append(float(features[0]))
        y.append(float(features[1]))
                
def linear_regres(x,y):
    xmean= sum(x)/len(x)
    ymean= sum(y)/len(y)

    n=len(x)
    YSum =sum(y)
    XSum =sum(x)

    XXSum = sum([a**2 for a in x])
    YYSum = sum([a**2 for a in y])
    XYSum = sum([a*b for (a,b) in zip(x,y)])
    x = [a-xmean for a in x]
    y = [a-ymean for a in y]
    slope1 = sum([a*b for a,b in zip(x,y)])/sum([a*a for a in x]);

    intercept1 =(YSum*XXSum - XSum*XYSum)/(n*XXSum - XSum**2)
    

    print(slope1*X + intercept1)

get_data()
print(linear_regres(x,y))