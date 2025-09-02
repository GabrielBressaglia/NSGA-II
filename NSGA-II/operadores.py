import numpy as np
import random
from populacao import Individuo
from parametros import *


def torneio(populacao):
    ind1: np.uint32 = np.random.randint(0, len(populacao) - 1)
    ind2: np.uint32 = np.random.randint(0, len(populacao) - 1)
    while(ind2 == ind1):
        ind2 = np.random.randint(0, len(populacao) - 1)

    if populacao[ind1].rank < populacao[ind2].rank:
        return ind1
    elif populacao[ind1].rank > populacao[ind2].rank:
        return ind2
    return ind1 if populacao[ind1].crowding_distance > populacao[ind2].crowding_distance else ind2

def crossover(ind_1, ind_2):
    if np.random.rand() < prob_crossover:  # Apenas realiza crossover com uma certa probabilidade
        filho_gene = (ind_1.gene + ind_2.gene)/2
    else:
        filho_gene = ind_1.gene.copy()  # Sem crossover, mantém o primeiro pai

    return Individuo(
        gene=filho_gene,
        fit_ind=np.zeros(num_obj, dtype=np.float64),
        crowding_distance=0.0,
        rank=0,
        contador_restricao=0
    )
def mutacao(ind, prob):
    mutation_prob = np.random.rand()

    if(mutation_prob < prob):
        ind.gene[random.randint(0, len(ind.gene) - 1)] += random.uniform(0.05, 0.05)
def makeNewPop(populacao):
    descendentes = []

    for i in range(len(populacao)):
        ind_1 = torneio(populacao)
        ind_2 = torneio(populacao)
        while(ind_2 == ind_1):
            ind_2 = torneio(populacao)

        filho = crossover(populacao[ind_1], populacao[ind_2])
        mutacao(filho, prob_mut)

        descendentes.append(filho)

    return descendentes