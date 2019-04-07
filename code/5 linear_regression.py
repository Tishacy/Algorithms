# -*- coding: utf-8 -*-
"""Multivariable Linear Regression

y = X * w
where   y is n×1 dimensioned, (output vector)
        X is n×m dimensioned，(m factors, input matrix)
        w is m×1 dimensioned. (parameter vector)

According to the Least Squared Method, the w vector could be calculated by the following equation.
w = (X^T * X)^(-1) * X^T * y
"""
import numpy as np

def multivariable_linear_regression(X, y):
    w = np.matmul(np.matmul(np.linalg.inv(
                np.matmul(np.transpose(X), X)
            ), np.transpose(X)), y)
    return w

def predict(X, w):
    return np.matmul(X, w)

if __name__=="__main__":
    # Generate original data
    n = 10  # number of sample data
    m = 5   # number of factors
    X_fit = np.random.rand(n, m)
    w_fit = np.arange(1, m+1)
    y_fit = np.matmul(X_fit, w_fit)
    print("The actual w vector is:\n", w_fit)

    # Fit the model
    w_fitted = multivariable_linear_regression(X_fit, y_fit)
    print("The fitted w vector is:\n", w_fitted)
