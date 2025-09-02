import numpy as np
from dataclasses import dataclass
from parametros import *

@dataclass
class Individuo:
    gene: np.ndarray
    fit_ind: np.ndarray
    crowding_distance: float
    rank: int
    contador_restricao: int

def gerar_pop():
    populacao = []

    for _ in range(num_pop):
        ind = Individuo(
            gene=np.zeros(num_genes, dtype=np.float64),  # Inicializa o array de genes
            fit_ind=np.zeros(num_obj, dtype=np.float64),  # Inicializa o fitness
            crowding_distance=0.0,
            rank=0,
            contador_restricao=0
        )
        ind.gene = np.array([np.random.uniform(0, 1) for _ in range(num_genes)], dtype=np.float64)
        #ind.gene = np.array([np.random.uniform(-5, 5) for _ in range(num_genes)], dtype=np.float64)
        populacao.append(ind)

    return populacao