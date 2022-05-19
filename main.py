
from Schwefel import Schewefel, mutatieUniforma, incrucisareConvexaSimpla, incrucisareMedie
import time

from Swarm import run10times






def run():
    start = time.time()
    i = int(input("alegeti: 1.Pb Schwefel, 2. Swarm Intelligence"))
    if i == 1:
        k = int(input("nr k"))
        nrGen = int(input("numar de generatii"))
        popSize = int(input("marime populatie"))
        n = int(input("dimensiune"))
        Schewefel(k, n, nrGen, popSize, mutatieUniforma, incrucisareMedie)


        time.sleep(1)
        end = time.time()
        with open('solutii.txt', 'a') as f:
            f.write(str({end - start}))
            f.write("\n")
    if i == 2:
        dim = int(input("Dim "))
        nrParticule = int(input("Nr particule "))
        iteratii = int(input("Marime generatie "))
        run10times(nrParticule, dim, iteratii)

        time.sleep(1)
        end = time.time()
        with open('solutii2.txt', 'a') as f:
            f.write(str({end - start}))
            f.write("\n")
run()