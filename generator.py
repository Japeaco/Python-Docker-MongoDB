import docker
import sys
import numpy
import time
import requests
import math

url = sys.argv[1]
dist = sys.argv[2]
mean = 0
stand = 0
lamb = 0
interval = 0
count = 0
lambone = 0
index = 0

if len(sys.argv) == 4 and dist == 'poisson':
    lamb = float(sys.argv[3])
    disno = numpy.random.exponential(lamb, 250)
    for x in disno:
        disnox = math.fabs(disno[index])
        r = requests.get(url)
        print(disnox)
        time.sleep(disnox)
        index += 1

elif len(sys.argv) == 5 and dist == 'normal':
    mean = float(sys.argv[3])
    stand = float(sys.argv[4])
    disno = numpy.random.normal(mean, stand, 250)
    for x in disno:
        disnox = math.fabs(disno[index])
        r = requests.get(url)
        print(disnox)
        time.sleep(disnox)
        index += 1

else:
    print("not enough arguments")