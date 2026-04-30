# Projeto Saite

Este projeto reúne um script Python para verificar se um número é primo e uma página HTML de apresentação. O foco principal é o arquivo `num_primo.py`, que implementa a lógica de detecção de números primos com validação de entrada e saída amigável.

## Arquivos principais

- `num_primo.py` - script Python que solicita um número inteiro, verifica se ele é primo e exibe o resultado.
- `index.html` - página estática sobre engenharia de prompt, com layout Bootstrap.
- `exolicacao_num_primo.md` - explicação técnica do algoritmo implementado em `num_primo.py`.
- `refatoracao.py/explicacao_refatoracao.md` - espaço reservado para documentação de refatoração.
- `teste-ass` - arquivo presente no diretório do projeto (sem conteúdo definido atualmente).

## Visão geral do script Python

O script `num_primo.py` contém as seguintes funções:

- `eh_primo(numero_inteiro: int) -> bool`:
  - Verifica se um número inteiro é primo.
  - Tratamento de casos especiais: números menores ou iguais a 1, 2 e 3.
  - Eliminação rápida de múltiplos de 2 e 3.
  - Uso de uma checagem eficiente de divisores na forma `6k ± 1`.

- `solicitar_numero_inteiro() -> int`:
  - Solicita que o usuário digite um número inteiro.
  - Repetição da solicitação até que a entrada seja válida.

- `exibir_resultado(numero_inteiro: int, primo: bool) -> None`:
  - Exibe no console se o número informado é primo ou não.

- `main() -> None`:
  - Orquestra o fluxo do programa: entrada, verificação e saída.

## Como executar

1. Abra um terminal no diretório do projeto.
2. Execute:

```bash
python num_primo.py
```

3. Digite um número inteiro quando solicitado.
4. O programa irá informar se o número `é primo` ou `não é primo`.

## Algoritmo de primalidade

A função `eh_primo` é otimizada para ser eficiente em relação ao tempo de execução:

- Retorna `False` imediatamente para valores `<= 1`.
- Retorna `True` para `2` e `3`, que são primos.
- Elimina números pares e múltiplos de 3 rapidamente.
- Percorre apenas possíveis divisores até a raiz quadrada do número.
- Testa apenas números na forma `6k - 1` e `6k + 1`, que são os únicos candidatos a primo além de 2 e 3.

## Informações adicionais

- O projeto não exige dependências externas além do Python 3.
- A página `index.html` pode ser aberta diretamente no navegador para visualizar o conteúdo de apresentação.
- O arquivo `exolicacao_num_primo.md` traz uma explicação detalhada do funcionamento do script.

## Sugestões de melhorias

- Adicionar testes automatizados para `eh_primo`.
- Integrar a lógica Python a uma interface web simples.
- Preencher o arquivo `refatoracao.py/explicacao_refatoracao.md` com notas de melhoria e refatoração.

---

Projeto criado para demonstrar lógica de verificação de números primos e documentação de código em Python.
