import ast

with open("modelScores.csv", 'r') as fp:
	data = fp.readlines()

for i in range(len(data)):
	data[i] = data[i].strip("\r\n")

xs = []
ys = []


for i in data:

	currList = ast.literal_eval(i)
	vector = currList[-1]
	
	print currList

	if currList[2] == "Eng":
		ys.append(1)
		xs.append(vector[:-1])

	elif currList[2] == "Hin":
		ys.append(0)
		xs.append(vector[:-1])


from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pickle

x = np.array(xs)
y = np.array(ys)

logreg = LogisticRegression()
logreg.fit(x, y)

with open('logres_classifier.pkl', 'wb') as fid:
    pickle.dump(logreg, fid)


print logreg.predict([[-1, -2, -3, -4]])

# use knn, K = 5
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# print metrics.accuracy_score(y_test, y_pred)

# # use knn, K = 1
# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# print metrics.accuracy_score(y_test, y_pred)

# # obtain highest accuracy by checking for all values of k

# # try K=1 through K=25 and record testing accuracy
# k_range = range(1, 26)
# scores = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_train, y_train)
#     y_pred = knn.predict(X_test)
#     scores.append(metrics.accuracy_score(y_test, y_pred))

# plt.plot(k_range, scores)
# plt.xlabel('Value of K for KNN')
# plt.ylabel('Testing Accuracy')
# plt.show()