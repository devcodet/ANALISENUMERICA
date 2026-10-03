
from Input import lerInput
from Processamento import converter


def main():
    try:
        # INPUT
        base_atual, numero, base_nova = lerInput()

        # PROCESSAMENTO - CONVERSÃO
        convertido = converter(numero, base_atual, base_nova)

        # OUTPUT - MOSTRAR RESULTADO
        print(f"{numero} NA BASE {base_atual}.")
        print(f"O número na base {base_nova} é {convertido}\n")

    except Exception as e:
        print(f"ERRO: {e}")


if __name__ == "__main__":
    main()
