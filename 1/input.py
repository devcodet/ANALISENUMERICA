import Numero

from Utilitarios import validacaoCaracteres


# LEITURA DA BASE ATUAL, NUMERO E BASE NOVA
def lerInput() -> Numero:
    # CICLO DE LEITURA E VALIDAÇÃO DA BASE ATUAL E DO NÚMERO A CONVERTER
    while True:
        try:
            base_atual = int(input("BASE ATUAL (2 a 62): "))
        except ValueError:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue

        if base_atual < 2 or base_atual > 62:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue

        numero = input("NUMERO: ")

        if not validacaoCaracteres(numero, base_atual):
            print(
                "Número incompatível com a base atual")
            continue
        break

    # CICLO DE LEITURA E VALIDAÇÃO DA NOVA BASE
    while True:
        try:
            base_nova = int(input("NOVA BASE (2 a 62): "))
        except ValueError:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue

        if base_nova < 2 or base_nova > 62:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue
        break

    # RETORNA UMA NOVA INSTÂNCIA DA CLASSE NUMERO COM OS DADOS VALIDADOS
    return Numero.Numero(base_atual, numero, base_nova, 0)
