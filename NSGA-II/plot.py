import matplotlib.pyplot as plt

def plot_grafico(populacao, fronts):
    plt.figure(figsize=(8, 6))

    fit1 =[]
    fit2 = []

    for i in fronts:
        fit1.append(populacao[i].fit_ind[0])
        fit2.append(populacao[i].fit_ind[1])

    plt.scatter(fit1, fit2, color='black', alpha=0.7)

    #plt.xlim(left=0)
    #plt.ylim(bottom=0)

    #plt.xlim(-20, -14)
    #plt.ylim(-12, 2)

    #plt.xlim(0, 1.1)
    #plt.ylim(0, 1.1)

    plt.xlabel("F1")
    plt.ylabel("F2")
    plt.title("NSGA-II")
    plt.legend()
    plt.grid(False)
    plt.show()