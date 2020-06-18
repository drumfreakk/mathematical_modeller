#!/usr/bin/python3

formule = lambda V : 0.19 * args.r * args.r * math.sqrt(V)

import matplotlib.pyplot as plt
import math
import argparse

parser = argparse.ArgumentParser(usage="%(prog)s [OPTIONS]", description="A simple simulation program for a bucket with a hole in it being filled with water")

parser.add_argument("-r", "--radius", type=float, default=0.5, metavar="R", help="radius of the hole in the bucket in cm (default: %(default)s)")
parser.add_argument("-f", "--flow", type=float, default=0.1, help="flow of water in to the bucket in L/s (default: %(default)s)")
parser.add_argument("-v", "--volume", type=float, default=10.0, help="volume of the bucket, L (default: %(default)s)")
parser.add_argument("-V", "--starting-volume", type=float, default=0.0, help="starting amount of water in the bucket, L (default: %(default)s)")
parser.add_argument("-c", "--chart", action="store_true", help="display the results in a chart in the terminal")
parser.add_argument("-d", "--datalimit", type=int, default=1000, help="set the amount of data to be displayed, with 1 for everything (default: %(default)s)")
parser.add_argument("-o", "--ofile", default="", help="file to write the output to (default: \"%(default)s\")")
parser.add_argument("-s", "--step", type=float, default=0.0001, help="time step, in seconds (default: %(default)s)")
parser.add_argument("-D", "--digits", type=int, default=3, help="digits to round the output to (default: %(default)s)")
parser.add_argument("-t", "--maxtime", type=int, default=100, help="maximum seconds to simulate (default: %(default)s)")

args = parser.parse_args()
print(args)

content = args.V

x = []
y = []
maxed = False          # Is de emmer vol
simSec = 0.0            # gesimuleerde secondes


def round_up(n, div=0):
	return n + (div - (n % div))


def round_dec(n, decimals=0):
	multiplier = 10 ** decimals
	return math.ceil(n * multiplier) / multiplier


while not maxed and simSec <= args.maxtime:
	x.append(simSec)
	y.append(content)
	content -= formule(content) * args.step
	content += args.f * args.step
	if content >= args.v:
		content = args.v
		maxed = True
	if content <= 0:
		content = 0.0
	# TODO: add on stable stop
	simSec += args.step

if args.ofile != "":
    f = open(args.ofile, "w")
    f.write("Tijd,args.Volume\n")
    for i in range(0, len(x), args.datalimit):
        f.write(str(x[i]) + "," + str(y[i]) + '\n')
    f.close()



if args.chart:
    print("_________________________________")
    print("|\tx\t|\ty\t|")
    print("|_______________________________|")
    for a in range(0, len(x), args.datalimit):
        print("|\t"+str(round_dec(x[a], args.digits))+"\t|\t"+str(round_dec(y[a], args.digits))+"\t|")
    print("|_______________________________|")
    exit()

if maxed:
	x.append(round_up(simSec, 10))
	y.append(y[-1])
	axis = [0, round_up(simSec, 10), 0, 11]
else:
	axis = [0, args.maxtime, 0, 11]

plt.plot(x, y)

plt.title('Emmer')
plt.ylabel('waterniveau (L)')
plt.xlabel('tijd (s)')
plt.axis(axis)
plt.grid(True)

plt.show()

