import random
import math

MIN_INT: float = -500
MAX_INT: float = 500

def fitness(n, x):
    f = 0
    for i in range(n):
        print("val x", x[i])
        c = math.sqrt(abs(x[i]))
        f = (-x[i]) * math.sin(c)
    print("functia f", f)
    return f


class Particula:
    def __init__(self, n):
        self.viteza = [random.uniform(MIN_INT, MAX_INT) for _ in range(n)]
        self.pozitie = [random.uniform(MIN_INT, MAX_INT) for _ in range(n)]
        self.currentFitness = fitness(n, self.pozitie)
        self.pbest = 10000

    def modificaViteza(self, gbest, w, c1, c2):
        for i in range(0, len(self.viteza)):
            self.viteza[i] = w * self.viteza[i] + c1 * random.random() * (self.pbest - self.pozitie[i]) + c2 * random.random() * (gbest - self.pozitie[i])

    def modificaPozitie(self):
        for i in range(0, len(self.pozitie)):
            self.pozitie[i] = self.pozitie[i] + self.viteza[i]
        self.currentFitness = fitness(len(self.pozitie), self.pozitie)

    def update_pbest(self):
        if self.currentFitness < self.pbest:
            self.pbest = self.currentFitness


    def setFitness(self):
        self.fitness = fitness(len(self.pozitie), self.pozitie)

    def setPbest(self, pbest1):
        self.pbest = pbest1

    def getFitness(self):
        return self.fitness

    def getPbest(self):
        return self.pbest


    def __repr__(self):
        return "x: " + str(self.pozitie) + " fitness: " + str(self.currentFitness) + " pbest: " + str(
            self.pbest) + " viteza: " + str(self.viteza) + "\n"