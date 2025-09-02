from populacao import gerar_pop
from funcao_objetivo import avaliar_pop, restricao_sch
from operadores import makeNewPop
from plot import plot_grafico
from parametros import *
from NSGA_utilidades import classificacaoNaoDominada, crowdingDistance
import numpy as np


def main():
    populacao = gerar_pop()

    time: np.uint32 = 0
    filhos = []

    while (time < c_parada):
        populacao.extend(filhos)

        for ind in populacao:
            ind.fit_ind = avaliar_pop(ind.gene)
        #restricao_sch(populacao)

        fronts = classificacaoNaoDominada(populacao)

        prox_geracao = []
        iterador = 0

        while len(prox_geracao) <= num_pop:
            if not fronts[iterador]:
                break
            crowdingDistance(populacao, fronts[iterador])
            for indx in fronts[iterador]:
                prox_geracao.append(populacao[indx])
            iterador += 1

        if len(prox_geracao) > num_pop:
            prox_geracao.sort(key=lambda ind: ind.crowding_distance, reverse=True)  # Ordena decrescentemente
            prox_geracao = prox_geracao[:num_pop]  # Mantém apenas os primeiros num_pop indivíduos

        filhos = makeNewPop(prox_geracao)

        populacao = prox_geracao

        time += 1

    respostas = classificacaoNaoDominada(populacao)

    plot_grafico(populacao, respostas[0])

    for ind in respostas[0]:
        print(populacao[ind].gene)

if __name__ == "__main__":
    main()