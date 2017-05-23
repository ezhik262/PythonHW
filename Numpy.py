import numpy as np
from scipy import optimize
from matplotlib import pylab as plt
x = np.arange(-10, 10, 0.04)

def f(x):
    return -0.5*x + 2 + 0.1*np.random.randn(len(x))
y = f(x)
plt.plot(x, y)#[f(a) for a in x] )
plt.show()
def Q(coeffs):
    k, b = coeffs
    return sum((y - k * x - b) ** 2)
y_min = optimize.minimize(Q, [5, 5])
print y_min.x