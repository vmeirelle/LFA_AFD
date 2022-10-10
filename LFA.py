def saidaConsole(existe):
    if(existe==True):
        print('S')
    else:
        print('N')

def validaCaractere(atual, alfabeto):
    for caractere in alfabeto:
        if(atual == caractere):
            return True
    return False

def validaEstado(atual, estados):
    for estado in estados:
        if(atual == estado):
            return True
    return False

def validaFinal(atual, finais):
    for final in finais:
        if(atual == final):
            return True
    return False

def estadoErro():
    return 'e'

def passoAFD(caractere, ocdLista, atual):
    for ocd in ocdLista:
        if(ocd[1]==caractere and atual[0]==ocd[0]):
            return ocd[2]
    return estadoErro()

def verificarPalavras(palavras, inicio, ocdLista,finais):
    verificacao = []
    for palavra in palavras:
        atual = inicio
        for caractere in palavra:
            atual = passoAFD(caractere, ocdLista, atual)
        verificacao.append(validaFinal(atual, finais))
    return verificacao

def inicio():

    estados = input().split(" ")
    alfabeto = input().split(" ")
    transicoes = int(input())
    ocd = []
    for i in range (transicoes):
        ocd.append(input().split(" "))
    inicio = input().split(" ")
    finais = input().split(" ")
    palavras = input().split(" ")
    
    resultado = verificarPalavras(palavras, inicio, ocd, finais)
    for k in range (0,len(resultado)):
        saidaConsole(resultado[k])

inicio()
