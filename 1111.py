import numpy as np
Func=lambda x, y:-np.sqrt(3+y**2,dtype=complex)/(y*np.sqrt(1-x**2,dtype=complex))
def rungeKutta(x0, y0, h):
    n = 1
    y = y0
    for i in range(1, n + 1):
        k1 = h * Func(x0, y)
        k2 = h * Func(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * Func(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * Func(x0 + h, y + k3)
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h
    return x0, y
epsilon=10**(-12)
x0 = 0
y = 5

h = 0.01
hmin=0.00000001

print(rungeKutta(x0, y, h))