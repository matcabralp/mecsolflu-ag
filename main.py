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
TOLERANCIA = 1e-12       # melhora mínima aceitável entre gerações
JANELA_TOLERANCIA = 10  # número de gerações observadas para avaliar convergência

# Fluxo principal
populacao = gerar_populacao(TAM_POPULACAO, D_MIN, D_MAX)

historico_melhor = []  # melhor fitness por geração
historico_media = []   # média do fitness por geração
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

    # Elitismo: garante que o melhor sobrevive
    nova_populacao[0] = melhor_atual
    populacao = nova_populacao

    # Coleta de dados para visualização e análise
    melhor_fitness_geracao = fitness(max(populacao, key=fitness))
    media_fitness_geracao = sum(fitness(d) for d in populacao) / len(populacao)
    historico_melhor.append(melhor_fitness_geracao)
    historico_media.append(media_fitness_geracao)

    print(f"Geração {geracao+1:03d} | Melhor: {melhor_fitness_geracao:.8f} | Média: {media_fitness_geracao:.8f}")

    # Critério de parada por tolerância
    # if verificar_tolerancia(historico_melhor, TOLERANCIA, JANELA_TOLERANCIA):
    #     print(f"\nConvergência atingida na geração {geracao+1} (tolerância={TOLERANCIA})")
    #     geracao_final = geracao + 1
    #     break

# Resultado final
melhor_d = max(populacao, key=fitness)
melhor_fitness = fitness(melhor_d)
vazao = 4.92 * melhor_d**2  # Q(d) = (pi*v2/4) * d^2

print(f"\n{'='*50}")
print(f"Diâmetro ótimo:       {melhor_d*1000:.4f} mm")
print(f"Função objetivo f(d): {melhor_fitness:.8f}")
print(f"Vazão correspondente: {vazao:.6f} m³/s")
print(f"Gerações executadas:  {geracao_final}")
print(f"{'='*50}")

# Visualizações
plotar_evolucao(historico_melhor, historico_media)
plotar_cromossomo(melhor_d, D_MIN, D_MAX)