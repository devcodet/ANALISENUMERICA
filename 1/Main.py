import Numero

from input import lerInput
from processamento import converter


def main():
    try:
        # INPUT - RECOLHER DADOS
        numero = lerInput()

        # PROCESSAMENTO - CONVERSÃO
        converter(numero)

        # OUTPUT - MOSTRAR RESULTADO
        print(f"ATUAL: {numero.valor_atual} NA BASE {numero.base_atual}")
        print(f"NOVO: {numero.valor_novo} NA BASE {numero.base_nova}")

    except Exception as e:
        print(f"ERRO: {e}")


if __name__ == "__main__":
    main()
