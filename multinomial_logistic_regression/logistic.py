import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# data from columns A - D study hours, classes ttended, CT1, CT2
Xtrain = np.array([[40,    35,   18,   20],
                   [30,    30,   12,   15],
                   [25,    32,   15,    6],
                   [28,    23,   10,   10],
                   [45,    30,   20,   16],
                   [35,    23,   10,   12],
                   [40,    30,   18,    4],
                   [30,    25,   12,   10]])

# data from column E - A, B, C, D
ytrain = np.array([1, 2, 3, 4, 1, 2, 3, 4])

lr = LogisticRegression().fit(Xtrain, ytrain)

yhat = lr.predict(Xtrain)

Xtest = np.array([[45,    30,   18,   16],
				  [30,    30,   15,    4]])

Ytest = lr.predict(Xtest)


print(yhat)
print(Ytest)

print(accuracy_score(ytrain, yhat)*100)

