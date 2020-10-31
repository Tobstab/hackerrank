# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
marks=[]

for i in range(2):
    marks.append(input().split("  "))
y=[]
x=[]

def get_data():
    for i in range(2):
        for j in range(1,11):
            if i == 1:
                y.append(int(marks[i][j]))
            else:
                x.append(int(marks[i][j]))

def get_slope(x,y):
    #mean
    Xsum=0
    Ysum=0
    XXsum =0
    YYsum =0
    XYsum=0
    for i in range(10):
        Xsum+=x[i]
        Ysum+=y[i]
        XXsum+=x[i]*x[i]
        YYsum+=y[i]*y[i]
        XYsum+=x[i]*y[i]

    Xmean=Xsum/10
    Ymean=Ysum/10
    SdeviationX = math.sqrt(((XXsum/10) -Xmean**2))
    SdeviationY = math.sqrt(((YYsum/10) -Ymean**2))
    slope = (10*(XYsum-(Xsum*Ysum)))/((XXsum**2)-(Xsum**2))
    print(slope)
    Yinter = Ymean -(Xmean*0.208)
    return (10*slope) -Yinter
        
get_data()

print(get_slope(x,y))
