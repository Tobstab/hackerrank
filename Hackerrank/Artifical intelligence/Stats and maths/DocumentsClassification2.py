# Enter your code here. Read input from STDIN.
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import json
#collect data and sort
ytrain=[]
xtrain=[]
with open('trainingdata.txt', 'r') as f:
    text=(f.read().split("\n"))
    count =0
    for i in range(1,int(text[0])):
        ytrain.append(text[i][0])
        xtrain.append(text[i][1:])
#print(text)
#sklearn pipeline
pipe = Pipeline([('cv', CountVectorizer(stop_words='english')),
                 ('tf',TfidfTransformer()),
                 ('clf',SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, random_state=42,
                                           max_iter=5, tol=None))])
#train the model
pipe.fit(xtrain,ytrain)

#predict model
n = int(input())
newStack=[]
for _ in range(n):
    newInput = input()
    print(newInput)
    newStack.append(newInput)
predict = pipe.predict(newStack)
print(*predict,sep='\n')


