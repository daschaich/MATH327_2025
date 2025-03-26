#!/usr/bin/python3
# ------------------------------------------------------------------
# Adapting from
# commons.wikimedia.org/wiki/File:Quantum_ideal_gas_pressure_3d.svg
import mpmath
import numpy as np
from matplotlib import pyplot as plt

# The mpmath polylog sometimes returns a tiny spurious imaginary part
# and it throws exceptions for weird cases. Clean this up.
def fixpoly(s,x):
  try:
    return np.real(mpmath.fp.polylog(s,x))
  except (OverflowError, ValueError):
    return np.nan
polylog = np.vectorize(fixpoly, otypes=[float])

alpha = 1.5

# Pressure vs temperature graph
fig = plt.figure()
fig.set_size_inches(4,2)
ax1 = plt.axes((0.09, 0.17, 0.90, 0.82))

# Fermi gas
color_fermi = '#1f77b4'
T_fermi = mpmath.fp.gamma(alpha+1) ** (1./alpha)
P_fermi = T_fermi / (alpha+1)

# Sweep z, making the last point to be basically T=0
z = np.exp(np.linspace(-2, 20, 201))
z[-1] = 1e100
T = (-polylog(alpha, -z)) ** (-1.0/alpha)
P = (T)**(alpha + 1) * -polylog(alpha + 1, -z)
S = (alpha + 1) * polylog(alpha + 1, -z) / polylog(alpha, -z) - np.log(z)
mu = np.log(z) * T

# Extend traces to exactly T=0
T = np.concatenate((T, [0.0]))
P = np.concatenate((P, [P_fermi]))

ax1.plot(T,P, label="Fermion gas", color=color_fermi)

# format temperature axis nicely
for ax in [ax1]:
  ax.set_xlim(0,1.8)
  ax.set_xlabel('T', labelpad=0)
  tl = []
  tl.append((0, "0", 'k'))
  ticks, labels, colors = zip(*tl)
  ax.set_xticks(ticks)
  ax.set_xticklabels(labels)
  for label,color in zip(ax.xaxis.get_ticklabels(), colors):
    label.set_color(color)

ax1.set_ylim(0,1.8)
ax1.set_yticks([0])
ax1.set_ylabel('P', rotation=0, labelpad=-5)
ax1.legend(loc='lower right')
#fig.show()
#fig.savefig('figs/unit08_pressure.pdf', bbox_inches='tight')
# ------------------------------------------------------------------
