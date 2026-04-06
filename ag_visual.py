import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from ag_continuo import fitness as fitness_continuo
from ag_discreto import fitness as fitness_discreto


# Constantes
D_MIN = 0.005
D_MAX = 0.040


def plotar_evolucao(historico_melhor, historico_media, titulo="Evolução do Fitness por Geração"):
    # Gráfico de evolução do fitness ao longo das gerações.
    # Mostra o melhor indivíduo e a média da população por geração.

    # Parâmetros:
    #     historico_melhor: lista com o melhor fitness de cada geração
    #     historico_media:  lista com a média do fitness de cada geração
    #     titulo:           título do gráfico
    geracoes = range(1, len(historico_melhor) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(geracoes, historico_melhor, label="Melhor indivíduo", color="royalblue", linewidth=2)
    plt.plot(geracoes, historico_media,  label="Média da população", color="tomato", linewidth=2, linestyle="--")

    plt.xlabel("Geração")
    plt.ylabel("Fitness f(d)")
    plt.title(titulo)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("evolucao_fitness.png", dpi=150)
    plt.show()
    print("Gráfico salvo: evolucao_fitness.png")


def plotar_cromossomo(melhor_d, d_min=D_MIN, d_max=D_MAX, titulo="Posição do Ótimo no Espaço de Busca"):
    """
    Visualização contínua: posição do diâmetro ótimo na curva f(d).

    Parâmetros:
        melhor_d: diâmetro ótimo encontrado pelo AG (em metros)
        d_min:    limite inferior do intervalo de busca
        d_max:    limite superior do intervalo de busca
        titulo:   título do gráfico
    """
    d_valores = np.linspace(d_min, d_max, 500)
    f_valores = [fitness_continuo(d) for d in d_valores]

    plt.figure(figsize=(10, 5))
    plt.plot(d_valores * 1000, f_valores, color="steelblue", linewidth=2, label="f(d)")
    plt.scatter(
        melhor_d * 1000,
        fitness_continuo(melhor_d),
        color="red", zorder=5, s=100,
        label=f"Ótimo AG: d = {melhor_d*1000:.4f} mm"
    )
    plt.axvline(melhor_d * 1000, color="red", linestyle="--", alpha=0.4)
    plt.axhline(0, color="black", linewidth=0.8, alpha=0.5)

    plt.xlabel("Diâmetro d (mm)")
    plt.ylabel("Fitness f(d)")
    plt.title(titulo)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("cromossomo_otimo.png", dpi=150)
    plt.show()
    print("Gráfico salvo: cromossomo_otimo.png")


def plotar_cromossomo_discreto(melhor_d, diametros_discretos, titulo="Posição do Ótimo no Espaço de Busca"):
    # Visualização discreta: mostra o fitness de cada diâmetro válido como barras,
    # destacando o ótimo encontrado pelo AG.

    # Parâmetros:
    #     melhor_d:            diâmetro ótimo encontrado pelo AG (em metros)
    #     diametros_discretos: lista com todos os diâmetros válidos (em metros)
    #     titulo:              título do gráfico


    d_mm  = [d * 1000 for d in diametros_discretos]
    f_vals = [fitness_discreto(d) for d in diametros_discretos]
    cores  = ["red" if d == melhor_d else "steelblue" for d in diametros_discretos]

    plt.figure(figsize=(10, 5))
    plt.bar(d_mm, f_vals, color=cores, width=2.5, edgecolor="black", linewidth=0.5)
    plt.axhline(0, color="black", linewidth=0.8, alpha=0.5)

    legenda = [
        Patch(color="red",       label=f"Ótimo AG: d = {melhor_d*1000:.0f} mm"),
        Patch(color="steelblue", label="Demais diâmetros"),
    ]
    plt.legend(handles=legenda)

    plt.xlabel("Diâmetro d (mm)")
    plt.ylabel("Fitness f(d)")
    plt.title(titulo)
    plt.xticks(d_mm)
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("cromossomo_otimo_discreto.png", dpi=150)
    plt.show()
    print("Gráfico salvo: cromossomo_otimo_discreto.png")