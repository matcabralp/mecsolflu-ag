def valor_vazao(d):
    vazao = (4.92 * d**2)-(10000 * d**4)
    return vazao

vazao_min = valor_vazao(0.005)
vazao_max = valor_vazao(0.040)
print(f"A vazao minima tem valor: {vazao_min}")
print(f"A vazao maxima tem valor: {vazao_max}")
