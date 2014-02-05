from numpy import array, dot
from numpy.linalg import inv

X = array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = array([[1], [2], [3], [4]])
n = inv(dot(X.T, X))
k = dot(X.T, y)
coef_ = dot(n, k)