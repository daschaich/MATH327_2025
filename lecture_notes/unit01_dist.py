#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
# ------------------------------------------------------------------
# Plot probability distribution from central limit theorem
# for simple 1d random walk with three values of (p, q) 
# Work mainly in terms of drift velocity and diffusion coefficient
# Have to use same number of colors and linestyles in cycler

# First no drift velocity, vdr = 0
p = 0.5
q = 1.0 - p
vdr = 2.0 * p - 1.0
DSq = 4.0 * p * q

x = np.arange(-6, 6, 0.01)
fig, ax = plt.subplots()
ax.set_prop_cycle(color=['k', 'b', 'g', 'r'], ls=["-", "--", "-.", ":"])
for t in range(1, 11):
  num = x - vdr * t
  denom = 2.0 * DSq * t
  coeff = 1.0 / np.sqrt(2.0 * np.pi * DSq * t)
  dist = coeff * np.exp(-num * num / denom)
  tag = "t = " + str(t)
  plt.plot(x, dist, marker='None', label=tag)
plt.axvline(0, linestyle='dotted', color='black', marker='None')
plt.legend(loc='upper right')
plt.title('Zero drift velocity: p = q = 0.5')
plt.xlabel('$x$')
plt.xlim([-6, 6])
plt.ylabel('$p(x)$')
plt.ylim([0, 0.5])

plt.savefig('figs/unit01_diff_zero.pdf', bbox_inches='tight')
#plt.show()
plt.clf()   # Clear figure

# Next low drift velocity, vdr = 0.2
p = 0.6
q = 1.0 - p
vdr = 2.0 * p - 1.0
DSq = 4.0 * p * q

x = np.arange(-6, 10, 0.01)
fig, ax = plt.subplots()
ax.set_prop_cycle(color=['k', 'b', 'g', 'r'], ls=["-", "--", "-.", ":"])
for t in range(1, 11):
  num = x - vdr * t
  denom = 2.0 * DSq * t
  coeff = 1.0 / np.sqrt(2.0 * np.pi * DSq * t)
  dist = coeff * np.exp(-num * num / denom)
  tag = "t = " + str(t)
  plt.plot(x, dist, marker='None', label=tag)
plt.axvline(0, linestyle='dotted', color='black', marker='None')
plt.legend(loc='upper right')
plt.title('Low drift velocity: p = 0.6, q = 0.4')
plt.xlabel('$x$')
plt.xlim([-6, 10])
plt.ylabel('$p(x)$')
plt.ylim([0, 0.5])

plt.savefig('figs/unit01_diff_low.pdf', bbox_inches='tight')
#plt.show()
plt.clf()   # Clear figure

# Finally high drift velocity, vdr = 0.98
p = 0.99
q = 1.0 - p
vdr = 2.0 * p - 1.0
DSq = 4.0 * p * q

x = np.arange(-6, 10, 0.01)
fig, ax = plt.subplots()
ax.set_prop_cycle(color=['k', 'b', 'g', 'r'], ls=["-", "--", "-.", ":"])
for t in range(1, 11):
  num = x - vdr * t
  denom = 2.0 * DSq * t
  coeff = 1.0 / np.sqrt(2.0 * np.pi * DSq * t)
  dist = coeff * np.exp(-num * num / denom)
  tag = "t = " + str(t)
  plt.plot(x, dist, marker='None', label=tag)
plt.axvline(0, linestyle='dotted', color='black', marker='None')
plt.legend(loc='upper right')
plt.title('High drift velocity: p = 0.99, q = 0.01')
plt.xlabel('$x$')
plt.xlim([-6, 10])
plt.ylabel('$p(x)$')
plt.ylim([0, 2.5])

plt.savefig('figs/unit01_diff_high.pdf', bbox_inches='tight')
#plt.show()
plt.clf()   # Clear figure
# ------------------------------------------------------------------
