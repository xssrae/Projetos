#importa a biblioteca random
from random import *

#usa a função randint (inicio, fim)
num = randint(0,20)

#variaveis auxiliares
i = 0 #contador de chutes
controle = 0  #flag, sinaliza que o número digitado é igual ao aleatório

while controle == 0:
    chute = int(input('Digite um número: '))
    i = i + 1 #i +=  1 / i++
    if num == chute:
        controle = 1 #altero a flag
        print('Parabéns, você acertou em', i, 'chutes')
    elif num > chute:
        print('O chute é menor do que o valor gerado')
    else:
        print('O chute é maior do que o valor gerado')
        