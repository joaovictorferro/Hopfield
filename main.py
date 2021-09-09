#Equipe:
# Arthur Savio
# Guilherme Amaral
# João Victor Ribeiro
# problema: Caixeiro Viajante
import numpy as np

entrada=[[0,7,5,3,1],
        [7,0,4,2,1],
        [5,4,0,5,3],
        [3,2,5,0,7],
        [1,1,3,7,0]]
global valor

dicionario = {0:"A",1:"B",2:"C",3:"D",4:"E"}

saidaA = [0,0,0,0,0]
saidaB = [0,0,0,0,0]
peso=[[0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]]

coluna_visitada=[0]

def inicializarPeso():
    for i in range(5):
        for j in range(5):
            if i != j:
                #Entradas da propria rede, nao sao entradas externas
                peso[i][j] = +0.001
            else:
                peso[i][j] = 0
        # entrada externa, ou seja, saida de nehum outro neuronio
        peso[i][5] = -0.001

def convergir_primeira_cidade():
    global valor
    valor = 0
    for index in range(5):
        print("INDEX: " + str(index))
        for i in range(5):
            soma = 0.0
            if i not in coluna_visitada:
                soma = entrada[valor][i] * peso[i][5] + 0.0000001
            for j in range(5):
                if j not in coluna_visitada:
                    soma = soma + saidaA[j] * peso[i][j]
            if i not in coluna_visitada:
                saidaB[i] = soma

        while True:
            valor = np.random.randint(0,5)
            #print(valor)
            if (valor not in coluna_visitada):
                break

        for k in range(len(saidaB)):
            if k not in coluna_visitada:
                if saidaB[k] > saidaB[valor]:
                    valor = k
        coluna_visitada.append(valor)
        print(coluna_visitada)
        if len(coluna_visitada) == 5:
            break;

def printSaidaA():
    for i in range(5):
        print(dicionario[coluna_visitada[i]] , end=" ")

if __name__ == '__main__':
    inicializarPeso()
    while True:
        convergir_primeira_cidade()
        c = 0
        flag = False
        for i in range(5):
            if saidaA[i] == saidaB[i]:
                c+= 1
        if c < 5:
            for j in range(5):
                saidaA[j] = saidaB[j]
            coluna_visitada.clear()
            coluna_visitada.append(0)
        else:
            flag = True;

        if flag:
            printSaidaA()
            break;
