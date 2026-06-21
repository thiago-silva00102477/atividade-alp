def classificar_prioridade(nivel_dor, tipo_lesao):
    if nivel_dor >= 4:
        return "ALTA"
    elif tipo_lesao == 2 or nivel_dor >= 3:
        return "MÉDIA"
    else:
        return "BAIXA"


def nome_tipo_lesao(tipo_lesao):
    if tipo_lesao == 1:
        return "Muscular"
    elif tipo_lesao == 2:
        return "Articular"
    elif tipo_lesao == 3:
        return "Corte/Contusão"
    else:
        return "Tipo inválido"


def main():
    print("=== SISTEMA DE TRIAGEM MÉDICA - TIME DE FUTEBOL ===\n")

    # Dados de entrada
    nome = "João"
    nivel_dor = 4
    tipo_lesao = 2

    # Validação dos dados
    if nivel_dor < 1 or nivel_dor > 5:
        print("Erro: o nível de dor deve estar entre 1 e 5.")
        return

    if tipo_lesao not in [1, 2, 3]:
        print("Erro: o tipo de lesão deve ser 1, 2 ou 3.")
        return

    # Processamento
    prioridade = classificar_prioridade(nivel_dor, tipo_lesao)
    lesao = nome_tipo_lesao(tipo_lesao)

    # Saída
    print("=== RESULTADO DA TRIAGEM ===")
    print(f"Nome do atleta: {nome}")
    print(f"Nível de dor: {nivel_dor}")
    print(f"Tipo de lesão: {lesao}")
    print(f"Prioridade do atendimento: {prioridade}")


main()