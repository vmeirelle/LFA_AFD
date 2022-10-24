
def saidaConsole(existe):
    if(existe==True):
        print('S')
    else:
        print('N')

def validaFinal(atuais, finais):
    for final in finais:
        for atual in atuais:
            if(atual == final):
                return True
    return False

def verificarPalavras(palavras, inicial, ocdHash,finalValido):

    verificacao = []

    for palavra in palavras:
        atual = [inicial]

        for caractere in palavra:
            destinos = []
            for i in atual:
                if(ocdHash[i].get(caractere)):
                    for j in range(0,len(ocdHash[i][caractere])):
                        if(ocdHash[i][caractere] not in destinos):
                            destinos.append(ocdHash[i][caractere][j])
            atual = destinos


        verificacao.append(validaFinal(atual, finalValido))

    return verificacao

def inicio():

    #Entradas
    estados = input().split(" ")
    alfabeto = input().split(" ")
    transicoes = int(input())

    ocd = {}
    for estado in estados:
        ocd[estado] = {}
    
    for i in range(0,transicoes):
        o, c, d = input().split(" ")
        if c not in ocd[o]:
            ocd[o][c] = []
        ocd[o][c].append(d)

    inicial = input()
    finais = input().split(" ")
    palavras = input().split(" ")
    
    #Chamada verificação
    resultado = verificarPalavras(palavras, inicial, ocd, finais)
    
    #Impressão
    for k in range (0,len(resultado)):
        saidaConsole(resultado[k])

inicio()

