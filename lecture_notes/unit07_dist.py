#!/usr/bin/python3
# ------------------------------------------------------------------
# Adapting from
# commons.wikimedia.org/wiki/File:Fermi-Dirac_Bose-Einstein_Maxwell-Boltzmann_statistics.svg
import numpy as np
import matplotlib.pyplot as plt

# Plot three distributions vs. x = beta * (E - mu)
pos = np.arange(0.01, 4.0, 0.01)
BE = 1.0 / (np.exp(pos) - 1)
x = np.arange(-4.0, 4.0, 0.01)
MB = 1.0 / np.exp(x)
FD = 1.0 / (np.exp(x) + 1)

plt.plot(pos, BE, linestyle="solid", label="Bose--Einstein", color="blue")
plt.plot(x, MB, linestyle="dashed", label="Maxwell--Boltzmann", color="red")
plt.plot(x, FD, linestyle="dotted", label="Fermi--Dirac", color="green")

plt.xlim(-4.0, 4.0)
plt.xlabel('$\\beta(E_{\ell} - \mu)$')
plt.ylim(0.0, 3.0)
plt.ylabel('$\left\langle n_{\ell} \\right\\rangle$', rotation=0, labelpad=15)
plt.legend(loc='upper right')
#plt.savefig('figs/unit07_dist.pdf', bbox_inches='tight')
#plt.show()
# ------------------------------------------------------------------
