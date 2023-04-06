# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Use formula in report to calculate general formula for R(t) and J(t) in case delta > 0
def visualization(a, b, c, d, R0, J0, tmax):
    Re_k = (a + d) / 2
    Im_k = (math.sqrt(abs(a*a + d*d - 2 * a * d + 4 * b * c)) / 2)
    K1 = Re_k + Im_k
    K2 = Re_k - Im_k
    C1 = ((K2 - d) * J0 - c * R0) / (K2 - K1)
    C2 = ((K1 - d) * J0 - c * R0) / (K1 - K2)
    def J(x):
        values = []
        for xval in x:
            s = C1 * math.exp(K1*xval) + C2 * math.exp(K2*xval)
            values.append(s)
        return values
    def R(x):
        values = []
        for xval in x:
            s = (C1 * (K1 - d) * math.exp(K1*xval) + C2 * (K2 - d) * math.exp(K2*xval)) / c
            values.append(s)
        return values
    x = np.linspace(0, tmax, 1000)
    return R(x), J(x), x