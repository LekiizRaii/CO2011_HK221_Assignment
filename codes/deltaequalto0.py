# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Use formula in report to calculate general formula for R(t) and J(t) in case delta == 0
def visualization(a, b, c, d, R0, J0, tmax):
    Re_k = (a + d) / 2
    K = Re_k
    C1 = J0
    C2 = (c * R0 - (K - d) * J0)
    def J(x):
        values = []
        for xval in x:
            s = C1 * math.exp(K*xval) + (C2 * xval * math.exp(K*xval))
            values.append(s)
        return values
    def R(x):
        values = []
        for xval in x:
            s = C1 * (K - d) * math.exp(K*xval) + (C2 * (1 + K * xval - d * xval) * math.exp(K*xval))/c
            values.append(s)
        return values
    x = np.linspace(0, tmax, 1000)
    return R(x), J(x), x