#!/usr/bin/python3

formule = lambda V : 0.19 * r_gat * r_gat * math.sqrt(V)

maxV = 10           # Inhoud emmer, L
V = 0.0             # Startwaarde inhoud emmer, L

toevoer_m = 9.0     # Watertoevoer, L/m
#toevoer = toevoer_m / 60      # Watertoevoer, L/s
toevoer = 0.1
r_gat = 0.5000      # radius gat, cm

maxSec = 100.0      # Max aantal gesimuleerde secondes
step = 0.0001      # Precisie, simulaties per seconde
toCSV = "" # Pad naar outputdocument, "" voor geen output
dataLimit = 1000    # Hoeveel van de data wordt opgeslagen/vertoond, 1 voor alles
digits = 3

import matplotlib.pyplot as plt
import math
import argparse

parser = argparse.ArgumentParser(usage="%(prog)s [OPTIONS]", description="A simple simulation program for a bucket with a hole in it being filled with water")
parser.add_argument("-r", type=float, default=r_gat, help="Radius of the hole in the bucket in cm (default: %(default)s)")
parser.add_argument("-f", type=float, default=toevoer, help="Flow of water in to the bucket in L/s (default: %(default)s)")
parser.add_argument("-v", type=float, default=maxV, help="Volume of the bucket, L (default: %(default)s)")
parser.add_argument("-V", type=float, default=V, help="Starting amount of water in the bucket, L (default: %(default)s)")
parser.add_argument("-c", "--chart", action="store_true", help="Display the results in a chart in the terminal")
parser.add_argument("-d", "--datalimit", type=int, default=dataLimit, help="Set the amount of data to be displayed, with 1 for everything (default: %(default)s)")
parser.add_argument("-o", "--ofile", default=toCSV, help="File to write the output to (default: \"%(default)s\")")
parser.add_argument("-s", "--step", type=float, default=step, help="Timestep, in seconds (default: %(default)s)")
parser.add_argument("-D", "--digits", type=int, default=digits, help="Digits to round the output to (default: %(default)s)")
parser.add_argument("-t", "--maxtime", type=int, default=maxSec, help="Maximum seconds to simulate (default: %(default)s)")

args = parser.parse_args()
chart = args.chart
dataLimit = args.datalimit
toCSV = args.ofile
step = args.step
digits = args.digits
maxSec = args.maxtime
r_gat = args.r
toevoer = args.f
maxV = args.v
V = args.V


x = []
y = []
maxed = False          # Is de emmer vol
simSec = 0.0            # gesimuleerde secondes


def round_up(n, div=0):
	return n + (div - (n % div))


def round_dec(n, decimals=0):
	multiplier = 10 ** decimals
	return math.ceil(n * multiplier) / multiplier


############################################################
######################## Simulatie #########################
############################################################

while not maxed and simSec <= maxSec:
	x.append(simSec)
	y.append(V)
	V -= formule(V) * step
	V += toevoer * step
	if V >= maxV:
		V = maxV
		maxed = True
	if V <= 0:
		V = 0.0
	# TODO: add on stable stop
	simSec += step

############################################################
###################### Einde simulatie #####################
############################################################

############################################################
###################### Grafiek maken #######################
############################################################

if toCSV != "":
    f = open(toCSV, "w")
    f.write("Tijd,Volume\n")
    for i in range(0, len(x), dataLimit):
        f.write(str(x[i]) + "," + str(y[i]) + '\n')
    f.close()



if chart:
    print("_________________________________")
    print("|\tx\t|\ty\t|")
    print("|_______________________________|")
    for a in range(0, len(x), dataLimit):
        print("|\t"+str(round_dec(x[a], digits))+"\t|\t"+str(round_dec(y[a], digits))+"\t|")
    print("|_______________________________|")
    exit()

if maxed:
	x.append(round_up(simSec, 10))
	y.append(y[-1])
	axis = [0, round_up(simSec, 10), 0, 11]
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
