#!/usr/bin/python3
# Initialization
import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt   # Convenient nickname
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# Pseudo-random numbers
random.seed(327)
u = random.random()
print(u)
print(random.random())

# Print both English text and general ('g') numbers,
# displaying six significant figures
# 'u' remains what it was set to be above!
print("Pseudo-random numbers: %.6g and %.6g" % (u, random.random()))
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# Inverse transform sampling and the 'for' loop
random.seed(327)
nSamples = int(2e6)
data = []
ave = 0.0
sqAve = 0.0
for i in range(0, nSamples):
  data.append(2.0 * math.sqrt(random.random()))
  ave += data[-1]     # Add to running sums
  sqAve += data[-1] * data[-1]

ave /= nSamples
sqAve /= nSamples
sigma = math.sqrt(sqAve - ave * ave)
print("\nmu = %.6g" % ave)
print("sigma = %.6g" % sigma)

# Check against exact analytic results
exact_mu = 4.0 / 3.0
diff = 100.0 * np.abs(1.0 - ave / exact_mu)       # Absolute value
print("\nMean within %.2g percent of exact result" % diff)

exact_sigma = math.sqrt(2.0) / 3.0
diff = 100.0 * np.abs(1.0 - sigma / exact_sigma)  # Overwrites diff
print("StDev within %.2g percent of exact result" % diff)

print("\nMean check: %.6g" % np.mean(data))
print("StDev check: %.6g" % np.std(data))
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# Histogram
nbins = 75
plt.hist(data, nbins, density=True, label='Data')
x = np.arange(0, 2, 0.01)   # Points 0, 0.01, ..., 1.99
y = 0.5 * x
plt.plot(x, y, 'r', label='y(x)')
plt.xlabel('$x$')
plt.ylabel('$p$')
plt.legend(loc='upper left')

# Save and/or show figure
# 'tight' reduces surrounding whitespace
plt.savefig('hist.pdf', bbox_inches='tight')
plt.show()
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# Random walks
num_steps = [10, 20, 30, 40, 50, 60, 70, 80]
nWalks = int(2e5)     # Number of times to repeat each walk
L = []
print("N  L")
for Nstep in num_steps:
  L.append(0.0)     # Array of running sums
  for i in range(0, nWalks):
    d = 0.0         # Single running sum
    for step in range(0, Nstep):
      d += 2.0 * math.sqrt(random.random())
    L[-1] += d
  L[-1] /= float(nWalks)
  print("%d %.3f" % (Nstep, L[-1]))

# Plot as small points (".") instead of a line
# Force the plot to include the origin
plt.xlim(0, 1.1*max(num_steps))
plt.ylim(0, 1.1*max(L))
plt.xlabel('Number of steps')
plt.ylabel('Average walk length')
plt.plot(num_steps, L, linestyle='None', marker=".")
plt.show()
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# Polynomial fit
output = np.polyfit(num_steps, L, 1)
a=output[-2]
b=output[-1]
print("a = %.6g" % a)
print("b = %.6g" % b)

# Replot the points, since show() reset the previous plot
plt.xlim(0, 1.1*max(num_steps))
plt.ylim(0, 1.1*max(L))
plt.xlabel('Number of steps')
plt.ylabel('Average walk length')
plt.plot(num_steps, L, linestyle='None', marker=".", label="Data")
x = np.arange(0, 80, 0.1)
p = a * x + b
plt.plot(x, p, 'r', label="Fit")
plt.legend(loc='lower right')
plt.show()
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# Trick to simplify power-law fits
logN = np.log(num_steps);
logL = np.log(L);
output = np.polyfit(logN, logL, 1)
alpha = output[-2]
c = np.exp(output[-1])
print("alpha = %.6g" % alpha)
print("c = %.6g" % c)

plt.xlim(0, 1.1*max(num_steps))
plt.ylim(0, 1.1*max(L))
plt.xlabel('Number of steps')
plt.ylabel('Average walk length')
plt.plot(num_steps, L, linestyle='None', marker=".", label="Data")
x = np.arange(0, 80, 0.1)
p = c * x**alpha
plt.plot(x, p, 'r', label="Fit")
plt.legend(loc='lower right')
plt.show()
# ------------------------------------------------------------------
