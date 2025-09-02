from parametros import *
import numpy as np


#Supoe minimizacao das duas FOs!
def verificarDominancia(ind_1, ind_2):
    melhorEmPeloMenosUm: bool = False

    for i in range(len(ind_1.fit_ind)):
        if (ind_1.fit_ind[i] > ind_2.fit_ind[i]):
            return False
        if (ind_1.fit_ind[i] < ind_2.fit_ind[i]):
            melhorEmPeloMenosUm = True

    return melhorEmPeloMenosUm

# Primeiro verifica se há passagem da proibicao. Depois o criterio e o fit
def dominacia_restricao(ind_1, ind_2):
    if ind_1.contador_restricao < ind_2.contador_restricao:
        return True
    elif ind_1.contador_restricao == 0 and ind_2.contador_restricao == 0:
        return verificarDominancia(ind_1, ind_2)
    else:
        return False


    return melhorEmPeloMenosUm
def classificacaoNaoDominada(populacao):
    S = [[] for _ in range(len(populacao))]
    n = [0] * len(populacao)
    fronts = [[]]

    for p in range(len(populacao)):
        for q in range(len(populacao)):
            if(dominacia_restricao(populacao[p], populacao[q])):
                S[p].append(q)
            elif(dominacia_restricao(populacao[q], populacao[p])):
                n[p] += 1
        if(n[p] == 0):
            populacao[p].rank = 0
            fronts[0].append(p)
    i: int = 0
    while(fronts[i]):
        nextFront = []

        for p in fronts[i]:
            for q in S[p]:
                n[q] -= 1
                if(n[q] == 0):
                    populacao[q].rank = i + 1
                    nextFront.append(q)
        i += 1
        fronts.append(nextFront)
    return fronts
def crowdingDistance(populacao, front):
    if len(front) == 0:
        return

    for idx in front:
        populacao[idx].crowding_distance = 0

    L = len(front)


    for m in range(num_obj):
        front.sort(key=lambda idx: populacao[idx].fit_ind[m])

        populacao[front[0]].crowding_distance = np.inf
        populacao[front[L - 1]].crowding_distance = np.inf
        fMin = populacao[front[0]].fit_ind[m]
        fMax = populacao[front[L - 1]].fit_ind[m]

        if fMax - fMin == 0:
            continue

        for i in range(1, L-1):
            prev = populacao[front[i - 1]].fit_ind[m]
            next = populacao[front[i + 1]].fit_ind[m]
            populacao[front[i]].crowding_distance += (next - prev) / (fMax - fMin)