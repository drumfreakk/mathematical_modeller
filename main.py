#!/usr/bin/python3

############################################################
######################## Variabelen ########################
####### verander deze om de simulatie te veranderen ########
############################################################

def formule(V):
	return 0.19 * r_gat * r_gat * math.sqrt(V)


maxV = 10           # Inhoud emmer, L
V = 0.0             # Startwaarde inhoud emmer, L
toevoer = 0.1       # Watertoevoer, L/s
r_gat = 0.5         # radius hole, cm

maxSec = 400.0      # Max aantal gesimuleerde secondes
sPerT = 1           # Precisie, simulaties per seconde

##################### EINDE VARIABELEN #####################
################# Verander niets hieronder #################
############################################################

############################################################
######### Functies en variabelen voor de simulatie #########
############################################################

import matplotlib.pyplot as plt
import math

x = []
y = []
maxxed = False          # Is de emmer vol
simSec = 0.0            # gesimuleerde secondes


def round_up(n, div=0):
	return n + (div - (n % div))


def round_dec(n, decimals=0):
	multiplier = 10 ** decimals
	return math.ceil(n * multiplier) / multiplier


############################################################
######################## Simulatie #########################
############################################################

while not maxxed and simSec < maxSec:
	x.append(simSec)
	y.append(V)
	V += toevoer * sPerT
	V -= formule(V) * sPerT
	if V >= maxV:
		V = maxV
		maxxed = True
	if V <= 0:
		V = 0.0
	# TODO: add on stable stop
	simSec += sPerT

############################################################
###################### Einde simulatie #####################
############################################################

############################################################
###################### Grafiek maken #######################
############################################################

if maxxed:
	x.append(round_up(simSec, 50))
	y.append(y[-1])
	axis = [0, round_up(simSec, 50), 0, 11]
else:
	axis = [0, maxSec, 0, 11]

plt.plot(x, y)

plt.title('Emmer')
plt.ylabel('waterniveau (L)')
plt.xlabel('tijd (s)')
plt.axis(axis)
plt.grid(True)

plt.show()

############################################################
######################## Einde code ########################
############################################################
