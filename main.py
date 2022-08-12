import re
import numpy as np

minValue = -9999999999999 #Controle para que a some nunca seja maior menor

def squareArray(array, start, finish, row):
    result = minValue
    soma = 0
    i = 0
    finish[0] = -1
    start_local = 0

    for i in range(row): #Loop carregado por fazer a soma e validar
        soma += array[i] 
        if soma < 0: #Caso a soma seja menor que zero resetar a soma e o i
            soma = 0
            start_local = i + 1
        elif soma > result:
            result = soma
            start[0] = start_local
            finish[0] = i

    if finish[0] != -1: #Caso a soma nao tenha sido apenas com numeros negativos
        return result

    result = array[0]
    start[0] = 0
    finish[0] = 0

    for i in range(1, row):
        if array[i] > result:
            result = array[i]
            start[0] = i
            finish[0] = i

    return result 

def subMatriz(matriz):
    col_len = len(matriz[1])
    row_len = len(matriz)
    maxSum = minValue
    left, top, right, bottom = 0,0,0,0
    
    controle = []
    start = [0]
    finish = [0]
    Sum = 0

    for colLeft in range(col_len):
        controle = [0] * row_len #Criar um array com o tamanho da coluna
        for colRight in range(colLeft, col_len):
            for row in range(row_len):
                controle[row] += matriz[row, colRight] #Adicionar o valor da coluna ao array
            Sum = squareArray(controle, start, finish, row_len)
            if Sum > maxSum:
                maxSum = Sum
                left = colLeft
                top = start[0]
                right = colRight
                bottom = finish[0]

    return left, top, right, bottom, maxSum

if __name__ == '__main__':
    m1 = np.random.randint(-10, 10, size=(2, 5))

    result = subMatriz(m1)

    print(f"""Primeira coordenada: {(result[0], result[1])}, 
Segunda coordenada: {(result[2], result[3])}, 
Soma Total: {result[4]}
Matriz:
{m1}
Valores: 
{m1[result[2]:result[3]+1, result[0]:result[1]+1]}""")