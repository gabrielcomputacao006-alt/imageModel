def eh_primo(numero_inteiro: int) -> bool:
    """Retorna True se o número informado for primo.

    Um número primo é divisível apenas por si mesmo e por 1.
    """
    if numero_inteiro <= 1:
        return False

    if numero_inteiro <= 3:
        return True

    if numero_inteiro % 2 == 0 or numero_inteiro % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= numero_inteiro:
        if numero_inteiro % divisor == 0 or numero_inteiro % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def solicitar_numero_inteiro() -> int:
    """Solicita ao usuário um valor inteiro até que a entrada seja válida."""
    while True:
        texto_entrada = input("Digite um número inteiro para verificar se é primo: ")
        try:
            return int(texto_entrada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def exibir_resultado(numero_inteiro: int, primo: bool) -> None:
    """Exibe o resultado da verificação de número primo."""
    status = "é primo" if primo else "não é primo"
    print(f"O número {numero_inteiro} {status}.")


def main() -> None:
    numero = solicitar_numero_inteiro()
    numero_eh_primo = eh_primo(numero)
    exibir_resultado(numero, numero_eh_primo)


if __name__ == "__main__":
    main()
