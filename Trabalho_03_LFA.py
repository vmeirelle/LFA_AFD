def consolePrint(existe):
    print('S') if existe==True else print('N')


def verificarPalavras(palavras, ini, apnd, fin):
    verificacao = []
    for palavra in palavras:
        current = [(ini, [], palavra)]
        check = False
        while check == False and len(palavra) > 0 and len(current) > 0:
            _est, _pil, _pal = current.pop()

            if apnd[_est].get('*') and _pal != '*':
                triplas = apnd[_est].get('*')
                for desempilha, estadoTo, empilha in triplas:
                    __pil = _pil.copy()
                    if desempilha != '*':
                        if len(__pil) == 0:
                            break
                        else:
                            topo = __pil.pop()
                            if desempilha != topo:
                                continue
                    if empilha != '*':
                        for element in empilha:
                            __pil.append(element)
                    current.append([estadoTo, __pil, _pal])
            if len(_pal) == 0:
                if _est in fin and len(_pil) == 0:
                    check = True
                else:
                    continue
            palavraTemp2 = _pal[1:]
            if apnd[_est].get(_pal[0]):
                triplas = apnd[_est].get(_pal[0])
                for desempilha, estadoTo, empilha in triplas:
                    pilhaTemporaria = _pil.copy()
                    if desempilha != '*':
                        if len(pilhaTemporaria) == 0:
                            break
                        else:
                            topo = pilhaTemporaria.pop()
                            if desempilha != topo:
                                continue
                    if empilha != '*':
                        for element in empilha:
                            pilhaTemporaria.append(element)
                    current.append([estadoTo, pilhaTemporaria, palavraTemp2])
        verificacao.append(check)
    return verificacao

def inicio():

    apnd = {}

    #Entradas
    estados = input().split(" ")
    for i in estados:
        apnd[i] = {}
    
    alfabeto = input().split(" ")
    alfabetoPilha = input().split(" ")
    transicoes = int(input())

    for i in range(0,transicoes):
        ini, let, des, fin, emp = input().split(" ")
        if let not in apnd[ini]:
            apnd[ini][let] = []
        apnd[ini][let].append([des, fin, emp])

    inicial = input()
    finais = input().split(" ")
    palavras = input().split(" ")
    
    #Chamada verificação
    resultado = verificarPalavras(palavras, inicial, apnd, finais)
    
    #Impressão
    for k in range (0,len(resultado)):
        consolePrint(resultado[k])

inicio()