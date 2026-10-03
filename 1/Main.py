import Numero

from Input import lerInput
from Processamento import converter


def main():
    try:
        # INPUT - RECOLHER DADOS
        numero = lerInput()

        # PROCESSAMENTO - CONVERSÃO
        numero.valor_novo = converter(
            numero.valor_atual,
            numero.base_atual,
            numero.base_nova)

        # OUTPUT - MOSTRAR RESULTADO
        print(f"{numero.valor_atual} NA BASE {numero.base_atual}.")
        print(f"O número na base {numero.base_nova} é {numero.valor_novo}\n")

    except Exception as e:
        print(f"ERRO: {e}")


if __name__ == "__main__":
    main()
