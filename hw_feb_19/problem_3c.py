from __future__ import division

import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt

def get_nth_term(n, t):
    def thing(x):
        return (((-1)**(n+1))/((2*n - 1)**2))*sin((2*n - 1)*pi*x)*cos((2*n - 1)*pi*t)
    return thing

def sum_to(N, t):
    def thing(x):
        SUM = 0
        for i in xrange(1, N+1):
            func = get_nth_term(i, t)
            SUM += func(x)
        return SUM*(8/(pi**2))
    return thing

final_time = 0.25
N1 = 5
N2 = 50
five = sum_to(N1, final_time)
fifty = sum_to(N2, final_time)

X = np.linspace(0, 1, 10000)
Y_1 = five(X)
Y_2 = fifty(X)

plt.figure()
plt.plot(X, Y_2, 'b-', linewidth=2, label=r"$N=%d$" % N2)
plt.plot(X, Y_1, 'r--', linewidth=2, label=r"$N=%d$" % N1)
plt.legend(loc=0)
plt.xlabel(r"$x$", size=15)
plt.ylabel(r"$u_N(x)$", size=15)
plt.title("t = %s" % str(final_time))
plt.savefig("problem_3c.png", format="png")
plt.show()
plt.close()