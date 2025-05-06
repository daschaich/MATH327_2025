#!/usr/bin/python3
import random
import time
import numpy as np
# ------------------------------------------------------------------
# Compute pi through Monte Carlo sampling
random.seed(271828)

# Loop over various numbers of samples
for N in [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9]:
  secs = -time.time()

  # Break each N into 20 chunks to monitor fluctuations
  bins = 20
  per_bin = int(N / bins)
  P = np.empty(bins, dtype = float)
  for B in range(bins):
    count = 0
    for i in range(per_bin):
      x = 2.0 * random.random() - 1.0
      y = 2.0 * random.random() - 1.0
      if (x*x + y*y < 1):
        count += 1

    P[B] = 4.0 * count / per_bin

  ave = np.mean(P)
  err = np.std(P)
  secs += time.time()
  print("%.0e samples --> pi=%.6g +/- %.4g in %.4g seconds" \
        % (N, ave, err, secs))
# ------------------------------------------------------------------
