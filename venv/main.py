#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math

def round_up(n, div=0):
    return n + (div - (n%div))

def round_dec(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


max = 10            # Inhoud emmer, L
waterniveau = 0.0   # Startwaarde inhoud emmer, L
toevoer = 0.1       # Watertoevoer, L/s
r_gat = 0.5          # radius hole, cm

maxSec = 400.0      # max seconds
sPerT = 1      # precision, steps per second

x = []
y = []
maxxed = False
iters = 0.0         # simulated seconds

while not maxxed and iters < maxSec:
    x.append(iters)
    y.append(waterniveau)
    waterniveau += toevoer * sPerT
    uitstroom = 0.19 * r_gat * r_gat * math.sqrt(waterniveau)
    waterniveau -= uitstroom * sPerT
    if (waterniveau >= max):
        waterniveau = max
        maxxed = True
    if (waterniveau <= 0):
        waterniveau = 0.0
    # TODO: add on stable stop
    iters += sPerT

if(maxxed):
    x.append(round_up(iters, 50))
    y.append(y[-1])
    axis = [0, round_up(iters, 50), 0, 11]
else:
    axis = [0, maxSec, 0, 11]

plt.plot(x, y)

plt.title('Emmer')
plt.ylabel('waterniveau (L)')
plt.xlabel('tijd (s)')
plt.axis(axis)
plt.grid(True)

plt.show()