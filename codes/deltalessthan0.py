# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Use formula in report to calculate general formula for R(t) and J(t) in case delta < 0
def visualization(a, b, c, d, R0, J0, tmax):
    Re_k = (a + d) / 2
    Im_k = (math.sqrt(abs(a*a + d*d - 2 * a * d + 4 * b * c)) / 2)
    C1 = J0
    C2 = (c * R0 - (Re_k - d) * J0) /Im_k
    def J(x):
        values = []
        for xval in x:
            s = math.exp(Re_k*xval) * (C1 * math.cos(Im_k*xval) + C2 * math.sin(Im_k*xval))
            values.append(s)
        return values
    def R(x):
        values = []
        for xval in x:
            s = ((Re_k-d) * math.exp(Re_k*xval) * (C1 * math.cos(Im_k*xval) + C2 * math.sin(Im_k*xval))
                + math.exp(Re_k*xval) * (C1 * Im_k * (-math.sin(Im_k*xval)) + C2 * Im_k * math.cos(Im_k*xval)))/c
            values.append(s)
        return values
    x = np.linspace(0, tmax, 1000)
    return R(x), J(x), x