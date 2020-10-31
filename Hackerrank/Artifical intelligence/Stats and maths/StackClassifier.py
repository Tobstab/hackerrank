# Enter your code here. Read input from STDIN.
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import json
#collect data and sort
ytrain=[]
xtrain=[]
with open('training.json', 'r') as f:
    count =0
    for line in f:
        count+=1
        if count > 1:
            post = json.loads(line)
            ytrain.append(post["topic"])
            xtrain.append(post["excerpt"])
#sklearn pipeline
pipe = Pipeline([('cv', CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')),
                 ('tf',TfidfTransformer()),
                 ('clf',MultinomialNB())])
#train the model
pipe.fit(xtrain,ytrain)

#predict model
n = int(input())
newStack=[]
for _ in range(n):
    newInput = json.loads(input())
    newStack.append(newInput['excerpt'])
predict = pipe.predict(newStack)
print(*predict,sep='\n')


