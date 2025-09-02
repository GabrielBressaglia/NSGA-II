import numpy as np

def avaliar_pop(genes):
    #ZDT2
    n = len(genes)

    f1 = genes[0]

    somatorio = np.sum(genes[1:])  # Soma de x₂ até xₙ
    g = 1 + 9 * somatorio / (n - 1)
    f2 = g * (1 - (genes[0] / g) ** 2)

    return np.array([f1, f2], dtype=np.float64)


    #KUR (-5, 5)
    """n = len(genes)

    fit1 = np.sum(-10 * np.exp(-0.2 * np.sqrt(genes[:-1] ** 2 + genes[1:] ** 2)))

    fit2 = np.sum(np.abs(genes) ** 0.8 + 5 * np.sin(genes ** 3))

    return np.array([fit1, fit2], dtype=np.float64)"""

    #SCH (-1000, 1000)
    """fit1: np.float64 = 0
    fit2: np.float64 = 0
    for i in range(len(genes)):
        fit1 += genes[i] * genes[i]
        fit2 += (genes[i] - 2) * (genes[i] - 2)

    return np.array([fit1, fit2], dtype=np.float64)"""

def restricao_sch(populacao):
    for ind in populacao:
        g = ind.gene
        if all(g > 1) or all(g < 0):
            ind.contador_restricao += 1