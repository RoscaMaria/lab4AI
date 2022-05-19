import Particula
import time

w = 1
c1 = 2
c2 = 2

def pso(nrParticule, dim, iteratii):
    k = 0
    particule = []
    gbest = 10000

    for i in range(0, nrParticule):
        particule.append(Particula.Particula(dim))
    print("particule", particule)

    while k < iteratii:
        for i in range(0, nrParticule):
            particule[i].update_pbest()

        for i in range(0, nrParticule):
            print("pbest", particule[i].getPbest())
            if particule[i].getPbest() < gbest:
                gbest = particule[i].getPbest()

        for i in range(0, nrParticule):
            particule[i].modificaViteza(gbest, w, c1, c2)
            particule[i].modificaPozitie()
        k = k + 1
    return gbest

def run10times(nrParticule, dim, iteratii):
    e = 0
    gbestAll = []
    sum =0
    best = 0
    while e < 10:
        gbest = pso(nrParticule, dim, iteratii)
        gbestAll.append(gbest)
        e = e + 1
    for i in range(len(gbestAll)):
        sum = sum + gbestAll[i]
        if gbestAll[i] < best:
            best = gbestAll[i]

    medie = sum / len(gbestAll)
    with open('solutii2.txt', 'a') as f:
        f.write("\n")
        f.write(str(dim))
        f.write(" ")
        f.write(str(iteratii))
        f.write(" ")
        f.write(str(nrParticule))
        f.write(" ")
        f.write(str(best))
        f.write(" ")
        f.write(str(medie))
        f.write(" ")
        f.write("\n")

