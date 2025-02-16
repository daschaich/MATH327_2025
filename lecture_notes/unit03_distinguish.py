#!/usr/bin/python3
# ------------------------------------------------------------------
# Plot energy and entropy for distinguishable spins
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01, 6.0, 0.01)
E = -np.tanh(1.0 / x)
S = -np.tanh(1.0 / x) / x + np.log(2.0 * np.cosh(1.0 / x))

high_x = [3.0, 6.0]
S_lim = [np.log(2.0), np.log(2.0)]
plt.plot(high_x, S_lim, 'b--', label="$\\log 2$")
plt.plot(x, S, 'b-', label="$S_D~/~N$")
plt.plot(x, E, 'r-.', label="$\\langle E\\rangle_D~/~NH$")
plt.xlabel('$\\frac{T}{H} = \\frac{1}{\\beta H}$', fontsize=16)
plt.xlim([0.0, 6.0])
plt.ylim([-1.0, 0.8])
plt.legend(loc='lower right')
plt.grid()
#plt.savefig('figs/unit03_distinguish.pdf', bbox_inches='tight')
plt.show()
# ------------------------------------------------------------------
