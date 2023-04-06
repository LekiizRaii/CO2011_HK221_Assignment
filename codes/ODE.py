import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

class ODE:
    # Initiate all values for the class
    def __init__(self, f, g, R_0 = 0, J_0 = 0, h = 0.01):
        self.__f = f
        self.__g = g
        self.__R0 = R_0
        self.__J0 = J_0
        self.__h = h

    # Get value from a time t
    def __getValue(self, R, J, t):
        R_ = self.__f(R, J, t)
        J_ = self.__g(R, J, t)
        return [R_, J_]

    # Newton-Raphson method for Backward Euler
    def __Newton_Raphson(self, R_pred, J_pred, t_next, R_n, J_n, delta, iterations = 100):
        def f0(R, J, t):
            return R - R_n - self.__f(R, J, t) * self.__h

        def f0_(R, J, t, diffOnR = True):
            if diffOnR:
                f0_0 = f0(R - delta / 2, J, t)
                f0_1 = f0(R + delta / 2, J, t)
            else:
                f0_0 = f0(R, J - delta / 2, t)
                f0_1 = f0(R, J + delta / 2, t)
            return (f0_1 - f0_0) / delta

        def f1(R, J, t):
            return J - J_n - self.__g(R, J, t) * self.__h

        def f1_(R, J, t, diffOnR = True):
            if diffOnR:
                f1_0 = f1(R - delta / 2, J, t)
                f1_1 = f1(R + delta / 2, J, t)
            else:
                f1_0 = f1(R, J - delta / 2, t)
                f1_1 = f1(R, J + delta / 2, t)
            return (f1_1 - f1_0) / delta

        x = np.array([R_pred, J_pred]).reshape(-1, 1)
        for i in range(iterations):
            R = x[0, 0]
            J = x[1, 0]
            Jacob =  np.zeros((2, 2))
            Jacob[0, 0] = f0_(R, J, t_next, True)
            Jacob[0, 1] = f0_(R, J, t_next, False)
            Jacob[1, 0] = f1_(R, J, t_next, True)
            Jacob[1, 1] = f1_(R, J, t_next, False)
            Jacob = inv(Jacob)
            F = np.array([f0(R, J, t_next), f1(R, J, t_next)]).reshape(-1, 1)
            x = x - Jacob.dot(F)
        return x[0, 0], x[1, 0]

    # Backward Euler method for approximating
    def Backward_Euler(self, iterations, delta = 0.01, visualize = False):
        listR = [self.__R0]
        listJ = [self.__J0]
        time = [0]
        t_next = 0
        for i in range(iterations):
            t_next = t_next + self.__h
            R_n = listR[len(listR) - 1]
            J_n = listJ[len(listJ) - 1]
            R_next, J_next = self.__Newton_Raphson(1, 1, t_next, R_n, J_n, delta)
            R_next = R_n + self.__f(R_next, J_next, t_next) * self.__h
            J_next = J_n + self.__g(R_next, J_next, t_next) * self.__h
            listR.append(R_next)
            listJ.append(J_next)
            time.append(t_next)

        # Used to visualize method if visualize = True
        if visualize:
            ax = plt.gca()
            ax.set_xticks(np.arange(min(time), max(time) + 1, 1))
            ax.set_xlabel("Time")
            ax.set_ylabel("Love for the other")
            ax.plot(time, listR)
            ax.plot(time, listJ)
            ax.legend(["Romeo's", "Juliet's"], loc=4)
            ax.set_title("LOVE BETWEEN ROMEO AND JULIET")

            plt.show()
        return np.array(listR), np.array(listJ), np.array(time)

    # Forward Euler method for approximating
    def Forward_Euler(self, iterations, visualize = False):
        listR = [self.__R0]
        listJ = [self.__J0]
        time = [0]
        t_next = 0
        for i in range(iterations):
            R_n = listR[len(listR) - 1]
            J_n = listJ[len(listJ) - 1]
            R_next = R_n + self.__f(R_n, J_n, t_next) * self.__h
            J_next = J_n + self.__g(R_n, J_n, t_next) * self.__h
            t_next = t_next + self.__h
            listR.append(R_next)
            listJ.append(J_next)
            time.append(t_next)

        # Used to visualize method if visualize = True
        if visualize:
            ax = plt.gca()
            ax.set_xticks(np.arange(min(time), max(time) + 1, 1))
            ax.set_xlabel("Time")
            ax.set_ylabel("Love for the other")
            ax.plot(time, listR)
            ax.plot(time, listJ)
            ax.legend(["Romeo's", "Juliet's"], loc = 4)
            ax.set_title("LOVE BETWEEN ROMEO AND JULIET")

            plt.show()
        return np.array(listR), np.array(listJ), np.array(time)







