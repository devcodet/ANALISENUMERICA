
from Utils import readInput


def main():

    while True:
        try:
            # Ler input do utilizador (número, base atual, nova base)
            number, current_base, new_base = readInput()

            # Converter o número da base atual para a nova base
            converted = convert(number, current_base, new_base)

            # Mostrar resultado
            print(f"\nConversão concluída com sucesso!")
            print(f"O número {number} está na base {current_base}.")
            print(f"O número na base {new_base} é {converted}\n")

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
