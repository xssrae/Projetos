from geopy.geocoders import Nominatim

def localPartida(partida):
    local = str(input("Endereço de partida: "))
    print(location.adress)
    print(location.latitude, location.longitude)

def localDestino():

def calcKM(km):    
    if km > 0 and km <= 15:
        corrida = 9.50 + (km*1.35)
        print()
        print(f'O valor a ser pago pela corrida é de: {corrida:.2f}')
    elif km >= 16 and km <= 20:
        corrida = 10.20 + (km*1.35)
        print()
        print(f'O valor a ser pago pela corrida é de: {corrida:.2f}')
        
    return corrida

print('Sistema de calculo de corrida iniciado')

