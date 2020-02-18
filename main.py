#!/usr/bin/python3

############################################################
######################## Variabelen ########################
####### verander deze om de simulatie te veranderen ########
############################################################

def formule(V):
	return 0.19 * r_gat * r_gat * math.sqrt(V)


maxV = 10           # Inhoud emmer, L
V = 0.0             # Startwaarde inhoud emmer, L
toevoer = 0.10      # Watertoevoer, L/s
r_gat = 0.0000      # radius hole, cm

maxSec = 400.0      # Max aantal gesimuleerde secondes
sPerT = 0.0001      # Precisie, simulaties per seconde
tabel = False        # Data in een tabel of een grafiek
toCSV = "./out.csv" # Pad naar outputdocument, "" voor geen output
dataLimiet = 1000    # Hoeveel van de data wordt opgeslagen/vertoond, 1 voor alles


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

if toCSV != "":
    f = open(toCSV, "w")
    f.write("Tijd,Volume\n")
    for i in range(0, len(x), dataLimiet):
        f.write(str(round_dec(x[i], 5)) + "," + str(round_dec(y[i], 5)) + '\n')
    f.close()



if tabel:
    print("__________________")
    print("|    x   |   y   |")
    for a in range(0, len(x), 10000):
        print("|\t"+str(x[a])+"\t|\t"+str(y[a])+"\t|")

    print("|________________|")
    exit()

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
