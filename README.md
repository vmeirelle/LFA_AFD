# LFA_AFD
Autômato Finito Determinístico

## 🔁 Algoritmo Simulador de AFD 🔁

A entrada consiste da especificação de um AFD e de um conjunto de palavras. A saída consiste de uma lista indicando ‘S’ caso o AFD reconheça a palavra em questão e ‘N’ caso contrário.

`passoAFD` A função passo do AFD, funciona para realizar os passos do AFD, andando do passo atual para o próximo, e retornando estado de erro caso o ocd (origem, caractere e destino), não conversem com o estado atual.

```python 
def passoAFD(caractere, ocdLista, atual):
    for ocd in ocdLista:
        if(ocd[1]==caractere and atual[0]==ocd[0]):
            return ocd[2]
    return estadoErro()
```

`validaFinal` A função válida final recebe como parâmetro o estado atual e a lista de estados finais. Nela é então verificado se o estado que se encontra é final.

```python
def validaFinal(atual, finais):
    for final in finais:
        if(atual == final):
            return True
    return False 
```
    
`verificarPalavras` A função verificar palavras recebe um conjunto de palavras, o estado de início, a lista de tuplas ocd, e os finais válidos. Então para cada palavra são realizados os passos do afd e validado o estado final dele. Então após realizar o mesmo para todas as palavras é retornado uma lista com o estado da verificação de cada palavra.

```python
def verificarPalavras(palavras, inicio, ocdLista,finais):
    verificacao = []
    for palavra in palavras:
        atual = inicio
        for caractere in palavra:
            atual = passoAFD(caractere, ocdLista, atual)
        verificacao.append(validaFinal(atual, finais))
    return verificacao
```
