def eh_primo(numero_inteiro: int) -> bool:
    """Verifica se um número inteiro é primo.

    Args:
        numero_inteiro: Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, caso contrário False.
    """
    if numero_inteiro <= 1:
        # Números menores ou iguais a 1 não são considerados primos.
        return False

    if numero_inteiro <= 3:
        # 2 e 3 são primos e já satisfazem os casos base.
        return True

    if numero_inteiro % 2 == 0 or numero_inteiro % 3 == 0:
        # Elimina múltiplos de 2 e 3 antes de usar a verificação mais cara.
        return False

    divisor = 5
    # Após eliminar 2 e 3, todos os primos restantes seguem a forma 6k ± 1.
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
            # Garante que o programa só prossiga com um inteiro válido.
            return int(texto_entrada)
        except ValueError:
            # Repeita a solicitação até que a entrada seja convertida com sucesso.
            print("Entrada inválida. Por favor, digite um número inteiro.")


def exibir_resultado(numero_inteiro: int, primo: bool) -> None:
    """Exibe o resultado da verificação de número primo."""
    status = "é primo" if primo else "não é primo"
    # Monta a mensagem final para deixar o resultado claro para o usuário.
    print(f"O número {numero_inteiro} {status}.")


def main() -> None:
    numero = solicitar_numero_inteiro()
    numero_eh_primo = eh_primo(numero)
    exibir_resultado(numero, numero_eh_primo)


if __name__ == "__main__":
    main()
