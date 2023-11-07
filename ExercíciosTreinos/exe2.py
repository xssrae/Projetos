#EXEMPLOS COM LISTAS E FUNÇÕES MAIS COMPOSTAS

def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x 
        return None
l=[10, 20, 22, 30]
print(pesquise(l, 22))
print(pesquise(l, 27))

print()
#############################################
# Listagem 8.6 – Cálculo da média de uma lista 
l = 0             # DEU CERTO: SIM() NÃO(x)
def soma(l):
    total=0
    for e in l:
        total+=e
        return total
    
def media(l):
    return(soma(l)/len(l))

print(media(34))

print()
#############################################

#LOCAIS E GLOBAIS

# EMPRESA = "Unidos Venceremos Ltda"
# def imprime_cabeçalho():
#    print(EMPRESA)
#    print("-" * len(EMPRESA))   
#A função imprime_cabeçalho não recebe parâmetros nem retorna valores. Ela simplesmente imprime
#o nome da empresa e traços abaixo dele.

a=5 #variável global
def muda_e_imprime():
    a=7 #variável local
    print("A dentro da função: %d" % a)
    print("a antes de mudar: %d" % a)  

muda_e_imprime() #chamada da função ^
print("a depois de mudar: %d" % a) # <- valor da variável global fora da função exibe o valor anterior normalmente.
# isso ocorre porque o pc entnede que são variáveis completamente diferentes.

#so burrra vei n e possivel. eu descobri o ngc de apoiar o teclado so agr.............e
#esse teclado é tão dlç...

print()
#############################################

# RECURSIVIDADE

def fatorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
    
print(fatorial(5))

print()
#############################################
