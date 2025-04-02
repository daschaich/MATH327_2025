#!/usr/bin/python3
# ------------------------------------------------------------------
# Check particle number consistency condition for
# non-relativistic fermion gas, given temperature and chemical potential
import sys
import numpy as np
from scipy import special, integrate
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (6,3)

# Parse arguments: Temperature t=T/E_F and chemical potential c=mu/E_F
#                  in units of the Fermi energy E_F
if len(sys.argv) < 3:
  print("Usage:", str(sys.argv[0]), "<T> <mu>")
  sys.exit(1)
t = float(sys.argv[1])        # Temperature t = T / E_F
c = float(sys.argv[2])        # Chemical potential c = mu / E_F

# Avoid repeatedly re-computing this
mu_exp = np.exp(-c / t)

# Rearrange integrand in terms of np.exp(-x) to avoid overflow
def integrand(x):
  num = np.sqrt(x) * np.exp(-x)
  denom = mu_exp + np.exp(-x)
  return num / denom

# Numerically integrate
one, max_err = integrate.quad(integrand, 0.0, np.inf)
one *= 1.5 * np.power(t, 1.5)
if one < 1.0:
  print("%.6g too low by %.4g" % (one, 1.0 - one))
else:
  print("%.6g too high by %.4g" % (one, one - 1.0))

# Plot some results
x = [];             y = []
x.append(0.1);      y.append(0.99)
x.append(0.2);      y.append(0.96)
x.append(0.4);      y.append(0.84)
x.append(0.6);      y.append(0.62)
x.append(0.8);      y.append(0.33)
x.append(1.0);      y.append(-0.02)
x.append(1.2);      y.append(-0.43)
x.append(1.4);      y.append(-0.88)
x.append(1.6);      y.append(-1.37)
x.append(1.8);      y.append(-1.90)
x.append(2.0);      y.append(-2.46)

plt.plot(x, y, 'rx')
leading_x = np.arange(0, 2.1, 0.01)
leading_y = 1.0 - (np.pi * leading_x)**2 / 12.0
plt.plot(leading_x, leading_y, 'g--')
plt.plot([0, 2.1], [0, 0], 'k-')
plt.xlabel('$T~/~E_F$')
plt.ylabel('$\\frac{\\mu}{E_F}$', rotation=0, fontsize=16, labelpad=10)
plt.xlim([0.0, 2.1])
plt.ylim([-2.6, 1.1])
#plt.show()
#plt.savefig('figs/unit08_fermi-gas.pdf', bbox_inches='tight')
# ------------------------------------------------------------------
