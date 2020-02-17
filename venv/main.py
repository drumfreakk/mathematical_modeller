import matplotlib.pyplot as plt
import numpy as np
import math

max = 10            # Inhoud emmer, L
waterniveau = 0.0   # Startwaarde inhoud emmer, L
toevoer = 0.1       # Watertoevoer, L/s

maxIters = 10000.0  # max calculations
tBeforeQuit = 5     # seconds where the bucket is filled before the sim stops

sPerT = 0.0001      # precision, steps per second
#rgat = 2

x = []
y = []
maxxed = 0
iters = 0.0

while maxxed < (tBeforeQuit / sPerT) and iters < maxIters:
    x.append(iters)
    y.append(waterniveau)
    #    uitstroom = 0.19 * rgat ** 2 * math.sqrt(waterniveau)
    waterniveau += toevoer * sPerT
    #    waterniveau -= uitstroom * sPerT
    if (waterniveau >= max):
        waterniveau = max
        maxxed += 1
    if (waterniveau <= 0):
        waterniveau = 0.0
    iters += sPerT

plt.plot(x, y)

plt.title('Emmer')
plt.ylabel('waterniveau (L)')
plt.xlabel('tijd (s)')

plt.show()