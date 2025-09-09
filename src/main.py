import control
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np


K = 3
T = 4
A = [[-1/T, 0], [0,0]]
B = [[K/T], [0]]
C = [[1, 0]]
D = 0

# A = [[0, 1], [-1, -3]]
# B = [[1], [0]]
# C = [[5,6]]
# D = [[1]]

def system_with_control_lib():
    ssmodel = control.ss(A, B, C, D)
    t, y = control.step_response(ssmodel)
    plt.plot(t, y)
    plt.title('Step response with Control')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()
    plt.show()

def system_with_scipy_lib():
    x0 = [0, 0]
    start = 0
    stop = 30
    step = 1
    t_b = np.arange(start, stop, step)
    ssmodel = signal.StateSpace(A, B, C, D)
    
    t, y = signal.step(ssmodel, x0, t_b)
    plt.plot(t, y)
    plt.title('Step response with Scipy')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # system_with_control_lib()
    system_with_scipy_lib()
