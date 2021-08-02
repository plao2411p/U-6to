
from types import LambdaType
import scipy
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def pendulum(y, t, b, c):
    theta, omega = y
    dydt = [
        omega,
        -b*omega - c*np.sin(theta)
    ]
    return dydt


b = 0.25
c = 5.0

y0 = [np.pi - 0.1, 0.0]
t = np.arange(0, 10, 0.02)

sol = odeint(pendulum, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig('solve-ode.svg')
