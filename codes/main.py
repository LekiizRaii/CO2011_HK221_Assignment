from ODE import *

# Function to compare approximating values to true values
def compare(listR, listJ, time):
    fig, axes = plt.subplots(1, 2, figsize = (10, 4))
    casR = np.exp(time) - 1
    casJ = np.exp(time)
    axes[0].plot(time, np.abs(listR - casR), linewidth = 1)
    axes[1].plot(time, np.abs(listJ - casJ), linewidth = 1)
    axes[0].set_title("On R")
    axes[1].set_title("On J")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Error")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Error")
    fig.suptitle("Absolute error between exact solution and Backward Euler method \n", fontsize = 16)
    plt.show()

# Function f(R, J, t) in formula
def f(R, J, t):
    return 2 * R + 3 * J

#Function g(R, J, t) in formula
def g(R, J, t):
    return 2 * R + 4 * J

S = ODE(f, g, -2, 3, 0.01)
listR, listJ, time = S.Backward_Euler(100, 0.01, True)