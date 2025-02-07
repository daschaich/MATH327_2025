#!/usr/bin/python3
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import special, integrate
# ------------------------------------------------------------------
# Compute and plot probabilities of roulette game outcomes
# comparing direct evaluation vs. the central limit theorem

# Parse argument: Number of spins
if len(sys.argv) < 2:
  print("Usage:", str(sys.argv[0]), "<spins>")
  sys.exit(1)
N = int(sys.argv[1])        # Number of spins

# Gain for W wins is 10W-5N, probability of winning is 18/37
p = 18.0 / 37.0             # Probability of winning each spin
q = 1.0 - p                 # Probability of losing each spin
delta_gain = 10             # Constant difference between subsequent gains
mean = -5.0 / 37.0          # Single-spin mean gain
var  = 25.0 - mean * mean   # Single-spin variance in gain

# For optional checking
print("For each spin the mean gain is %.6g " % mean, end=''),
print("with standard deviation %.6g" % np.sqrt(var))

# Directly evaluate probabilities of winning
# 'N + 1' to include both all wins and all losses
# binom(N, k) is N-choose-k binomial coefficient,
# which overflows double-precision floating-point numbers for N=1030, k~515
gain = np.empty(N + 1)
prob = np.empty_like(gain)
for W in range(N + 1):
  gain[W] = 10 * W - 5 * N
  prob[W] = special.binom(N, W) * np.power(p, W) * np.power(q, N - W)

  # For optional checking
  if gain[W] < 0.0:
    print("Probability %.6g to lose %d" % (prob[W], -1.0 * gain[W]))
  else:
    print("Probability %.6g to gain %d" % (prob[W], gain[W]))
print("Probabilities sum to %.6g" % np.sum(prob))

# Estimate probabilities from central limit theorem (CLT)
# This is the CLT probability *distribution* for N spins:
def CLT(x):
  num = (x - N * mean)**2
  denom = 2.0 * N * var
  coeff = 1.0 / np.sqrt(2.0 * np.pi * N * var)
  return coeff * np.exp(-1.0 * num / denom)

# First approximate probability as central value of integrand
# times (constant) difference between subsequent gains
print("\nConstant approximation:")
const = np.empty_like(prob)
for W in range(N + 1):
  const[W] = CLT(gain[W]) * delta_gain

  # For optional checking
  if gain[W] < 0.0:
    print("Probability %.6g to lose %d" % (const[W], -1.0 * gain[W]))
  else:
    print("Probability %.6g to gain %d" % (const[W], gain[W]))
print("Probabilities sum to %.6g" % np.sum(const))

# Next more accurately approximate probability
# by numerically integrating around central value
# Ignore upper bound on numerical integration error returned by quad
print("\nIntegrated approximation:")
delta_ov2 = 0.5 * delta_gain
integ = np.empty_like(prob)
for W in range(N + 1):
  lower = float(gain[W]) - delta_ov2
  upper = float(gain[W]) + delta_ov2
  integ[W], max_err = integrate.quad(CLT, lower, upper)

  # For optional checking
  if gain[W] < 0.0:
    print("Probability %.6g to lose %d" % (integ[W], -1.0 * gain[W]))
  else:
    print("Probability %.6g to gain %d" % (integ[W], gain[W]))
print("Probabilities sum to %.6g" % np.sum(integ))

# Plot all three data sets using matplotlib.pyplot ('plt')
# 'mfc' is short for markerfacecolor; 'none' gives an empty symbol
plt.figure(figsize=(6.40, 3.84))    # Standard Gnuplot size
plt.plot(gain, prob, 'go', mfc='none', label='Exact')   # Green circles
plt.plot(gain, integ, 'b+', label='Integrated')         # Blue pluses
plt.plot(gain, const, 'rx', label='Constant')           # Red x's

# If we forget to integrate the probability distribution,
# we will see the following incorrect results
#x = np.arange(gain[0], gain[N], 0.1)
#y = CLT(x)
#plt.plot(x, y, label='Distribution')

# Include zero at bottom without changing auto-scaled top
bottom, top = plt.ylim()
plt.ylim(0, top)

title = "N=" + str(N) + " spins of the roulette wheel"
plt.title(title)
plt.xlabel('Gain')
plt.ylabel('Probability')
plt.grid()
plt.legend()

# Optionally save pdf --- 'tight' reduces surrounding whitespace
#plt.savefig('figs/roulette_prob.pdf', bbox_inches='tight')
plt.show()
# ------------------------------------------------------------------
