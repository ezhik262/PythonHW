import inline as inline
import matplotlib
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import minimize
L = 50
x = np.linspace(-5, 5, 50)
def true_poly(x):
    return 0.1*x**4 + 0.2*x**3 - 0.25*x**2 + 2*x - 1
y = true_poly(x)
print x,y
%matplotlib inline
y_with_noise = y+6*np.random.randn(L)
plt.plot(x, y_with_noise)
plt.show

def poly(x, coeffs):
    return sum([coeffs[k]*x**k for k in range(len(coeffs))])
poly(1, [0.1, 4, 0.2, -0.25, 2, -1][::-1])
C=0
def loss(coeffs):
    loss = 0.0
    for a, b in zip(x, y_with_noise):
        loss += sum((poly(x, coeffs) - y_with_noise) **2)
    loss += C*sum(coeffs**2)
    return loss
result = minimize(loss, np.array([0.001]*(20)))
plt.plot(x, y_with_noise)
x_detailed = np.linspace(-5,5,500)
plt.plot(x_detailed, poly(x_detailed, result.x))
plt.show


