import numpy as np
import matplotlib.pyplot as plt
from ag_continuo import fitness

# Constantes
D_MIN = 0.005
D_MAX = 0.040


def plotar_evolucao(historico_melhor, historico_media):
    # Gráfico de evolução do fitness ao longo das gerações.
    # Mostra o melhor indivíduo e a média da população por geração.

    # Parâmetros:
    #   historico_melhor: lista com o melhor fitness de cada geração
    #   historico_media:  lista com a média do fitness de cada geração
    
    geracoes = range(1, len(historico_melhor) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(geracoes, historico_melhor, label="Melhor indivíduo", color="royalblue", linewidth=2)
    plt.plot(geracoes, historico_media,  label="Média da população", color="tomato",    linewidth=2, linestyle="--")

    plt.xlabel("Geração")
    plt.ylabel("Fitness f(d)")
    plt.title("Evolução do Fitness por Geração")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("evolucao_fitness.png", dpi=150)
    plt.show()
    print("Gráfico salvo: evolucao_fitness.png")


def plotar_cromossomo(melhor_d, d_min=D_MIN, d_max=D_MAX):
    # Visualização do cromossomo: posição do diâmetro ótimo na curva f(d).
    # Mostra onde o AG convergiu em relação ao espaço de busca completo.

    # Parâmetros:
    #   melhor_d: diâmetro ótimo encontrado pelo AG (em metros)
    #   d_min:    limite inferior do intervalo de busca
    #   d_max:    limite superior do intervalo de busca
    
    # Curva contínua de f(d) para todo o intervalo
    d_valores = np.linspace(d_min, d_max, 500)
    f_valores = [fitness(d) for d in d_valores]

    plt.figure(figsize=(10, 5))
    plt.plot(d_valores * 1000, f_valores, color="steelblue", linewidth=2, label="f(d)")

    # Marca o ponto ótimo encontrado pelo AG
    plt.scatter(
        melhor_d * 1000,
        fitness(melhor_d),
        color="red",
        zorder=5,
        s=100,
        label=f"Ótimo AG: d = {melhor_d*1000:.4f} mm"
    )

    # Linha vertical tracejada no ótimo
    plt.axvline(melhor_d * 1000, color="red", linestyle="--", alpha=0.4)

    # Linha horizontal no zero para referência
    plt.axhline(0, color="black", linewidth=0.8, alpha=0.5)

    plt.xlabel("Diâmetro d (mm)")
    plt.ylabel("Fitness f(d)")
    plt.title("Posição do Ótimo no Espaço de Busca (Cromossomo)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("cromossomo_otimo.png", dpi=150)
    plt.show()
    print("Gráfico salvo: cromossomo_otimo.png")