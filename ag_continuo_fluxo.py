from ag_continuo import gerar_populacao, fitness, selecao_natural, crossover, mutacao, verificar_tolerancia
from ag_visual import plotar_evolucao, plotar_cromossomo

# Parâmetros do problema
D_MIN = 0.005
D_MAX = 0.040

# Parâmetros do AG
TAM_POPULACAO = 50
TAM_SELECAO = 8
NUM_GERACOES = 100
TAXA_MUTACAO = 0.005
TOLERANCIA = None       # coloca None para desativar, ou ex: 1e-8 para ativar
JANELA_TOLERANCIA = 10  # número de gerações observadas para avaliar convergência


def executar():
    populacao = gerar_populacao(TAM_POPULACAO, D_MIN, D_MAX)

    historico_melhor = []
    historico_media = []
    geracao_final = NUM_GERACOES

    for geracao in range(NUM_GERACOES):
        melhor_atual = max(populacao, key=fitness)  # Elitismo

        nova_populacao = []
        for _ in range(TAM_POPULACAO):
            pai1 = selecao_natural(populacao, TAM_SELECAO)
            pai2 = selecao_natural(populacao, TAM_SELECAO)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho, TAXA_MUTACAO, D_MIN, D_MAX)
            nova_populacao.append(filho)

        nova_populacao[0] = melhor_atual  # Elitismo: garante que o melhor sobrevive
        populacao = nova_populacao

        melhor_fitness_geracao = fitness(max(populacao, key=fitness))
        media_fitness_geracao = sum(fitness(d) for d in populacao) / len(populacao)
        historico_melhor.append(melhor_fitness_geracao)
        historico_media.append(media_fitness_geracao)

        print(f"Geração {geracao+1:03d} | Melhor: {melhor_fitness_geracao:.8f} | Média: {media_fitness_geracao:.8f}")

        if TOLERANCIA and verificar_tolerancia(historico_melhor, TOLERANCIA, JANELA_TOLERANCIA):
            print(f"\nConvergência atingida na geração {geracao+1} (tolerância={TOLERANCIA})")
            geracao_final = geracao + 1
            break

    melhor_d = max(populacao, key=fitness)
    melhor_fitness = fitness(melhor_d)
    vazao = 4.92 * melhor_d**2  # Q(d) = (pi*v2/4) * d^2

    print(f"\n{'='*50}")
    print(f"[Contínuo] Diâmetro ótimo:       {melhor_d*1000:.4f} mm")
    print(f"[Contínuo] Função objetivo f(d): {melhor_fitness:.8f}")
    print(f"[Contínuo] Vazão correspondente: {vazao:.6f} m³/s")
    print(f"[Contínuo] Gerações executadas:  {geracao_final}")
    print(f"{'='*50}")

    plotar_evolucao(historico_melhor, historico_media, titulo="[Contínuo] Evolução do Fitness por Geração")
    plotar_cromossomo(melhor_d, D_MIN, D_MAX, titulo="[Contínuo] Posição do Ótimo no Espaço de Busca")