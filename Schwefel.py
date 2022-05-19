import math
import random
import numpy as np
import time
import matplotlib.pyplot as plt

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

def solRandom(n):
    return [random.uniform(MIN_INT, MAX_INT) for _ in range(n)]

def initializarePop(popSize, n):
    pop = []
    for i in range(popSize):
        pop.append(solRandom(n))
    return pop

def incrucisareConvexaSimpla(x, y, n):
    pos = np.random.randint(n)
    alpha = random.random()
    print(pos)
    print(alpha)
    xcopy = x.copy()
    ycopy = y.copy()
    for i in range(pos, n):
        x[i] = alpha * xcopy[i] + (1 - alpha) * ycopy[i]
        y[i] = alpha * ycopy[i] + (1 - alpha) * xcopy[i]

        if x[i] < MIN_INT:
            x[i] = MIN_INT
        if x[i] > MAX_INT:
            x[i] = MAX_INT
        if y[i] < MIN_INT:
            y[i] = MIN_INT
        if y[i] > MAX_INT:
            y[i] = MAX_INT

    return x, y

def incrucisareMedie(x, y, n):
    i = np.random.randint(n, size=2)
    print(i)
    xcopy = x.copy()
    x[i[0]] = (x[i[0]] + y[i[0]]) / 2
    y[i[0]] = (xcopy[i[0]] + y[i[0]]) / 2

    if x[i[0]] < MIN_INT:
        x[i[0]] = MIN_INT
    if x[i[0]] > MAX_INT:
        x[i[0]] = MAX_INT
    if y[i[0]] < MIN_INT:
        y[i[0]] = MIN_INT
    if y[i[0]] > MAX_INT:
        y[i[0]] = MAX_INT

    x[i[1]] = (x[i[1]] + y[i[1]]) / 2
    y[i[1]] = (xcopy[i[1]] + y[i[1]]) / 2

    if x[i[1]] < MIN_INT:
        x[i[1]] = MIN_INT
    if x[i[1]] > MAX_INT:
        x[i[1]] = MAX_INT
    if y[i[1]] < MIN_INT:
        y[i[1]] = MIN_INT
    if y[i[1]] > MAX_INT:
        y[i[1]] = MAX_INT


def mutatieUniforma(x, t):
    for i in range(len(x)):
        if random.random() < 0.3:
            x[i] = random.uniform(MIN_INT, MAX_INT)
    return x



def selectieTurnir(pop, popSize):
    sample = np.random.default_rng().choice(popSize, size=5, replace=False)
    best = pop[sample[0]].copy()
    for i in sample:
        if fitness(len(pop[i]), pop[i]) < fitness(len(best), best):
            best = pop[i].copy()
    return best

def bestAll(n,  best):
    for j in range(len(best)-1):
        for i in range(len(best) - j -1):

            if fitness(n, best[i]) < fitness(n, best[i + 1]):
                best[i], best[i + 1] = best[i + 1], best[i]
    return best

def bestOfGenerations(pop, copii, copiiMutanti, d):
    popConc = copii + pop + copiiMutanti
    for j in range(1, 10):
        for i in range(10 - j):
            if fitness(d, popConc[i]) < fitness(d, popConc[i+1]):
                popConc[i], popConc[i + 1] = popConc[i + 1], popConc[i]
    return popConc

def mediePop(pop, n):
    sum = 0.0

    for i in range(0, len(pop)):

        print("normal pop ", pop[i])
        print("fitnss medie1", fitness(n, pop[i]))

        sum = sum + fitness(n, pop[i])

    medie = sum/len(pop)
    print("best medie din fct", medie)
    return medie

def plots(best, worst, n):
    best_fit = []
    worst_fit = []
    for i in range(len(best)):
        best_fit.append(fitness(n, best[i]))
        worst_fit.append(fitness(n, worst[i]))
        print("best fit", best_fit)
    plt.figure()
    plt.title("Evolutia algoritmului")
    plt.plot(best_fit, 'g')
    plt.plot(worst_fit, 'r')
    plt.show()

def Schewefel(k, n, nrGen, popSize, mutatie, incrucisare):
    exec = 0

    bestOfAll = []
    worstOfAll = []
    averageAll = []
    bestMedie = []
    worstMedie = []
    while exec < k:
        pop = initializarePop(popSize, n)
        best = []
        worst = []
        average = []
        t = 0
        while t < nrGen:
            copii = []
            for i in range(popSize // 2):
                parinte1 = selectieTurnir(pop, popSize)
                parinte2 = selectieTurnir(pop, popSize)
                copil1, copil2 = incrucisareConvexaSimpla(parinte1, parinte2, n)

                copii.append(copil1)
                copii.append(copil2)
            copiiMutanti = []
            for i in range(len(copii)):
                mutant = mutatie(copii[i], t)
                copiiMutanti.append(mutant)
            pop = bestOfGenerations(pop, copii, copiiMutanti, n)
            best.append(pop[-1])
            worst.append(pop[0])
            average.append(mediePop(pop, n))
            t = t + 1
        medie = 0
        print("best", best)
        print("worst", worst)
        for i in range(0, len(average)):
            medie = medie + average[i]
        medie = medie / len(average)
        averageAll.append(medie)
        bestOfAll = bestAll(n, best)
        fctFList = []
        for i in range(len(bestOfAll)):
            fctFList.append(fitness(n, bestOfAll[i]))

            print("mean best of all", bestOfAll[i])
        print("fctList", fctFList)
        print("fitness all best 1", fitness(n, bestOfAll[0]))
        print("fitness all best 2", fitness(n, bestOfAll[len(bestOfAll) - 1]))
        print("len all best", len(bestOfAll))
        allBest1 = best[len(bestOfAll) - 1]
        allWorst = bestOfAll[0]
        print("all best", bestOfAll)
        print("all worst", allWorst)
        print("all best 1", allBest1)
        bestSol = fitness(n, allBest1)
        worstSol = fitness(n, allWorst)
        print("best sol", bestSol)
        print("medie", medie)
        print("worst sol", worstSol)
        print("best", best)
        print("worst", worst)
        bestMedie.append(mediePop(bestOfAll, n))
        for i in range(len(bestOfAll)):
            print("all best 1 in for", bestOfAll[i])
            print("fitness all best 1 in for", fitness(n, bestOfAll[i]))


        bestMedie1 = MAX_INT
        for i in range(len(bestMedie)):
            if bestMedie[i] < bestMedie1:
                bestMedie1 = bestMedie[i]
        print("best medie", bestMedie1)
        print("best medie list", bestMedie)

        exec = exec + 1

    plots(best, worst, n)
    with open('solutii.txt', 'a') as f:
        f.write("\n")
        f.write("best sol " + str(bestSol))
        f.write(" ")
        f.write("worts sol " + str(worstSol))
        f.write(" ")
        f.write("medies " + str(medie))
        f.write(" ")
        f.write("best medie " + str(bestMedie1))
        f.write(" ")
        f.write("nr gen " + str(nrGen))
        f.write(" ")
        f.write("pop size " + str(popSize))
        f.write(" ")
        f.write("\n")