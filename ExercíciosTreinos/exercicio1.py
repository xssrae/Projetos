#Escreva uma função que retorne o maior de dois números:  
# DEU CERTO: SIM(X) NÃO( )

from re import I


def maior(a,b):
    if a>b:
        maior_n = a
        return(print(maior_n))
    elif a<b:
        maior_n = b
        return(print(maior_n))

maior(5,3)

#############################################

#Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo: 
# DEU CERTO: SIM(X) NÃO( )

def multiple(a,b):
    if a%b == 0:
        return(True)
    else:
        return(False)
    
print(multiple(50,2))

#############################################
#Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado2):
# DEU CERTO: SIM(x) NÃO( )

def area_quadrado():
    l = int(input('Digite o valor de um lado do quadrado:'))
    lado = l**2
    return(lado)

print(area_quadrado())


#Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2).
# DEU CERTO: SIM(x) NÃO( )

tri = 0
def area_tri():
    b = int(input('Digite o valor da base: '))
    a = int(input('Digite o valor da altura: '))
    tri = (b*a)/2
    return(tri)

area_tri()
print(tri)

