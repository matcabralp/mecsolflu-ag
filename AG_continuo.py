import random

# Geração de populações
def gerar_populacao(tam_populacao, diametro_min, diametro_max):
    populacao = []
    for _ in range(tam_populacao):
        individuo = random.uniform(diametro_min, diametro_max)
        populacao.append(individuo)
    return populacao

# populacao = gerar_populacao(20, 0.005, 0.040)
# print("Populacao gerada:")
# for individuo in populacao:
#     print(f"{individuo:.6f}")


# Cálculo do fitness individual
def fitness(d):
    return (4.92 * d**2) - (10000 * d**4)

# valores_fitness = [fitness(individuo) for individuo in populacao]
# print("\nFitness dos individuos:")
# for individuo, fit in zip(populacao, valores_fitness):
#     print(f"Individuo: {individuo:.6f}, Fitness: {fit:.6f}")


# Seleção natural
def selecao_natural(populacao, num_selecionados):
    competidores = random.sample(populacao, num_selecionados)
    return max(competidores, key=fitness)

# print("\nIndividuo selecionado por selecao natural:")
# individuo_selecionado = selecao_natural(populacao, 20)
# print(f"{individuo_selecionado:.6f}")


# Crossover
def crossover(pai1, pai2):
    alfa = random.random() # retorna um numero aleatorio entre 0 e 1
    filho = (alfa * pai1) + ((1 - alfa) * pai2)
    return filho
    # O filho é uma combinação linear dos pais, onde alfa determina a contribuição de cada pai
    # Esse operador de crossover tem nome formal: BLX-α (Blend Crossover), introduzido por Eshelman e Schaffer (1993). 
    # É uma referência clássica em computação evolutiva, que está sendo usada aqui, em outro contexto, como um peso.

# pai1 = selecao_natural(populacao, 3)
# pai2 = selecao_natural(populacao, 3)
# filho = crossover(pai1, pai2)
# print(f"Pai 1:  d={pai1:.6f}, f(d)={fitness(pai1):.6f}")
# print(f"Pai 2:  d={pai2:.6f}, f(d)={fitness(pai2):.6f}")
# print(f"Filho:  d={filho:.6f}, f(d)={fitness(filho):.6f}")


# Mutação
def mutacao(individuo, taxa_mutacao, diametro_min, diametro_max):
    if random.random() < taxa_mutacao:
        amplitude_mutacao = diametro_max - diametro_min
        perturbacao = random.uniform(-0.1 * amplitude_mutacao, 0.1 * amplitude_mutacao)
        individuo += perturbacao
        individuo = max(min(individuo, diametro_max), diametro_min) # Garantir que o indivíduo permaneça dentro dos limites (Clamping)
    return individuo

# filho_mutado = mutacao(filho, 0.005, 0.005, 0.040)
# print(f"Filho mutado:  d={filho_mutado:.6f}, f(d)={fitness(filho_mutado):.6f}")


# Critério de parada por tolerância
def verificar_tolerancia(historico_melhor, tolerancia, janela):
    # Verifica se o AG convergiu observando as últimas 'janela' gerações.
    # Retorna True se a melhora máxima nesse período for menor que a tolerância.

    # Parâmetros:
    # historico_melhor: lista com o melhor fitness de cada geração
    # tolerancia: melhora mínima aceitável para continuar evoluindo
    # janela: número de gerações recentes a observar (padrão: 10)
    
    if len(historico_melhor) < janela:
        return False  # Ainda não há gerações suficientes para avaliar
    ultimas_geracoes = historico_melhor[-janela:]
    melhora = max(ultimas_geracoes) - min(ultimas_geracoes)
    return melhora < tolerancia