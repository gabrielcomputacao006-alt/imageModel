# Explicação do código em `num_primo.py`

## Função `eh_primo(numero)`

```python
def eh_primo(numero: int) -> bool:
```
- Define a função `eh_primo` com um tipo de entrada `int` e saída `bool`.
- O tipo ajuda a deixar o código mais claro e ajuda editores a detectar erros.

```python
    """Verifica se um número inteiro é primo.

    Retorna True quando o número for primo e False caso contrário.
    """
```
- Docstring explicando o propósito da função.
- Essa documentação está diretamente no código e melhora a legibilidade.

```python
    if numero <= 1:
        return False
```
- Verifica se `numero` é menor ou igual a 1.
- Números primos são definidos apenas para inteiros maiores que 1.

```python
    if numero <= 3:
        return True
```
- Retorna `True` para 2 e 3.
- Esses dois valores são casos especiais e são tratados logo no começo.

```python
    if numero % 2 == 0 or numero % 3 == 0:
        return False
```
- Remove todos os múltiplos de 2 e 3.
- O operador `%` calcula o resto da divisão.
- Essa verificação torna o código mais eficiente antes de entrar no laço principal.

```python
    divisor = 5
```
- Declara `divisor` com um nome descritivo em vez de `i`.
- Nomes claros ajudam a entender o papel da variável.

```python
    while divisor * divisor <= numero:
```
- Continua o laço enquanto o quadrado do divisor for menor ou igual a `numero`.
- Não é preciso testar divisores maiores do que a raiz quadrada.

```python
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return False
```
- Testa se `numero` é divisível por `divisor` ou por `divisor + 2`.
- Isso verifica pares de candidatos do tipo `6k - 1` e `6k + 1`.
- Se encontrar um divisor, retorna `False`.

```python
        divisor += 6
```
- Avança `divisor` de 6 em 6.
- Mantém o padrão de testar somente candidatos que podem ser primos.

```python
    return True
```
- Retorna `True` quando nenhum divisor válido foi encontrado.
- Indica que `numero` é primo.

## Função `main()`

```python
def main() -> None:
```
- Cria uma função separada para a execução principal do script.
- Isso melhora a organização e permite reutilizar `eh_primo` sem rodar o teste automático.

```python
    while True:
        entrada = input("Digite um número inteiro para verificar se é primo: ")
        try:
            numero = int(entrada)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
```
- Solicita que o usuário digite um número inteiro.
- Valida a entrada com `int(entrada)` dentro de um `try/except`.
- Em caso de erro de conversão, pede novamente um valor válido.

```python
    resultado = eh_primo(numero)
    mensagem = "é primo" if resultado else "não é primo"
    print(f"O número {numero} {mensagem}.")
```
- Chama a função `eh_primo` com o número informado pelo usuário.
- Usa uma variável intermediária (`mensagem`) para deixar o código mais legível.
- A f-string imprime o resultado formatado em uma frase clara.

## Bloco de execução direta

```python
if __name__ == "__main__":
    main()
```
- Garante que `main()` seja executada somente quando o arquivo for rodado diretamente.
- Se o módulo for importado em outro arquivo, o bloco não será executado.

## Mudanças de Clean Code aplicadas

- melhor nome de variável: `divisor` em vez de `i`;
- separação da lógica de execução em `main()`;
- tipos de entrada/saída na assinatura da função;
- mensagem formatada em variável intermediária para facilitar leitura;
- docstring mais clara e explicativa.

## Resumo técnico

- Valida casos especiais primeiro (`<= 1`, `2`, `3`).
- Elimina múltiplos de 2 e 3 rapidamente.
- Testa apenas divisores do tipo `6k - 1` e `6k + 1`.
- Usa a raiz quadrada como limite de busca para eficiência.
