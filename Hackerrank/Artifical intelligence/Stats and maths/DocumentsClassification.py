# Enter your code here. Read input from STDIN. Print output to STDOUT

txt = open("trainingdata.txt").read()
documents = txt.split("\n")
x_traindata = []
y_traindata =[]

for i in range(len(documents)-1):
    if i > 0:
        x_traindata.append(documents[i][2:])
        y_traindata.append(documents[i][0])

#bag of words method, dictonary each word and count up occurences of words
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
x_train_counts = count_vect.fit_transform(x_traindata)
x_train_counts.shape

#unbiased frequency of terms in a text
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(x_train_counts)
x_train_tf = tf_transformer.transform(x_train_counts)
x_train_tf.shape

#train the classifier
