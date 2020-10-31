# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
marks=[]
if input() != "":
    for i in range(2):
        marks.append(input().split("  "))

#XY
XYsum =0
XXsum =0
YYsum =0
Xsum=0
Ysum=0
for y in range(0,10):
    XYsum+=int(marks[0][y])*int(marks[1][y])
    XXsum+=int(marks[0][y])*int(marks[0][y])
    YYsum+=int(marks[1][y])*int(marks[1][y])
    Xsum+=int(marks[0][y])
    Ysum+=int(marks[1][y])
#print(XYsum,YYsum,Xsum,Ysum,XXsum)
#mean
Xmean=Xsum/10
Ymean=Ysum/10
#covariance - the average deviation from the mean for each respective mean
covar = (XYsum/10) -(Xmean*Ymean)
#print(covar)
#standard deviation
SdeviationX = math.sqrt(((XXsum/10) -Xmean**2))
SdeviationY = math.sqrt(((YYsum/10) -Ymean**2))
#print(SdeviationX,SdeviationY)
#Correlation coefficient
r = covar/(SdeviationX*SdeviationY)
print("%.3f"%(r))
