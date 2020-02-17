import matplotlib.pyplot as plt
import numpy as np
import math

def round_up(n, div=0):
    return n + (div - (n%div))

max = 10            # Inhoud emmer, L
waterniveau = 0.0   # Startwaarde inhoud emmer, L
toevoer = 0.1       # Watertoevoer, L/s

maxIters = 10000.0  # max calculations

sPerT = 0.0001      # precision, steps per second
#rgat = 2

x = []
y = []
maxxed = False
iters = 0.0

while not maxxed and iters < maxIters:
    x.append(iters)
    y.append(waterniveau)
    #    uitstroom = 0.19 * rgat ** 2 * math.sqrt(waterniveau)
    waterniveau += toevoer * sPerT
    #    waterniveau -= uitstroom * sPerT
    if (waterniveau >= max):
        waterniveau = max
        maxxed = True
    if (waterniveau <= 0):
        waterniveau = 0.0
    iters += sPerT


x.append(round_up(iters, 50))
y.append(y[-1])

plt.plot(x, y)

plt.title('Emmer')
plt.ylabel('waterniveau (L)')
plt.xlabel('tijd (s)')
plt.axis([0, round_up(iters, 50), 0, 11])
plt.grid(True)

plt.show()