#EXEMPLOS COM FUNÇÕES SIMPLES

def par(x):
    return(x%2==0)  #pares


def par_ou_impar(x): #comparação de pares e ímpares
    if par(x): 
        return "par"
    else:
        return "ímpar"
print(par_ou_impar(4)) #saída comum
print(par_ou_impar(5))