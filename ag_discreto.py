import random

# Diâmetros discretos
DIAMETROS_DISCRETOS = [0.005, 0.009, 0.013, 0.017, 0.021, 0.025, 0.029, 0.033, 0.037]


# Cálculo do fitness
def fitness(d):
    return (4.92 * d**2) - (10000 * d**4)


# Geração de população: cada indivíduo é um valor do conjunto discreto
def gerar_populacao(tam_populacao):
    return [random.choice(DIAMETROS_DISCRETOS) for _ in range(tam_populacao)]


# Seleção por torneio: sorteia k indivíduos e retorna o de maior fitness
def selecao_natural(populacao, num_selecionados):
    competidores = random.sample(populacao, num_selecionados)
    return max(competidores, key=fitness)


def crossover(pai1, pai2):
    # Crossover discreto: sorteia aleatoriamente o valor de um dos dois pais.
    # Diferente do caso contínuo, a média ponderada não é usada aqui porque
    # o resultado poderia não pertencer ao conjunto discreto de diâmetros válidos.
    filho = random.choice([pai1, pai2])
    return filho


def mutacao(individuo, taxa_mutacao):
    # Mutação discreta: substitui o indivíduo por um valor aleatório do conjunto,
    # diferente do atual. O clamping não é necessário pois o conjunto já é finito.
    if random.random() < taxa_mutacao:
        candidatos = [d for d in DIAMETROS_DISCRETOS if d != individuo]
        return random.choice(candidatos)
    return individuo


def verificar_tolerancia(historico_melhor, tolerancia, janela=10):
    # Verifica se o AG convergiu observando as últimas 'janela' gerações.
    # Retorna True se a melhora máxima nesse período for menor que a tolerância.

    # Parâmetros:
    #     historico_melhor: lista com o melhor fitness de cada geração
    #     tolerancia: melhora mínima aceitável para continuar evoluindo
    #     janela: número de gerações recentes a observar (padrão: 10)
    if len(historico_melhor) < janela:
        return False
    ultimas_geracoes = historico_melhor[-janela:]
    melhora = max(ultimas_geracoes) - min(ultimas_geracoes)
    return melhora < tolerancia