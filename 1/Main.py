
from Input import lerInput
from Processamento import converter


def main():
    while True:
        try:
            # Ler input do utilizador (número, base atual, nova base)
            numero, atual_base, nova_base = lerInput()

            # Converter o número da base atual para a nova base
            convertido = converter(numero, atual_base, nova_base)

            # Mostrar resultado
            print(f"\nConversão concluída com sucesso!")
            print(f"O número {numero} está na base {atual_base}.")
            print(f"O número na base {nova_base} é {convertido}\n")

        except Exception as e:
            # Captura qualquer erro inesperado e informa o utilizador
            print(f"Ocorreu um erro durante a conversão: {e}")
            print("Por favor, tente novamente.\n")
            continue  # Volta ao início do loop sem quebrar o programa

        # Perguntar se o utilizador quer continuar
        exit_input = input("Pretende continuar a converter? (S/N): ")
        if exit_input.upper() == "N":
            print("Programa terminado. Obrigado por utilizar o conversor!")
            break


if __name__ == "__main__":
    main()
