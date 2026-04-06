import ag_continuo_fluxo
import ag_discreto_fluxo

OPCOES = {
    "a": ("Letra a) — AG com diâmetro contínuo [5, 40] mm", ag_continuo_fluxo.executar),
    "b": ("Letra b) — AG com diâmetro discreto {5, 9, 13, ..., 37} mm", ag_discreto_fluxo.executar),
}

def main():
    print("=" * 50)
    print("  Atividade 4 — Bocal de saída e AG")
    print("=" * 50)
    for chave, (descricao, _) in OPCOES.items():
        print(f"  [{chave}] {descricao}")
    print("=" * 50)

    escolha = input("\nEscolha a alternativa (a/b): ").strip().lower()

    if escolha not in OPCOES:
        print("Opção inválida. Execute novamente e escolha 'a' ou 'b'.")
        return

    print(f"\nExecutando {OPCOES[escolha][0]}...\n")
    OPCOES[escolha][1]()  # chama executar() do fluxo escolhido

if __name__ == "__main__":
    main()