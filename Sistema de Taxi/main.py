#função que retorna a localização do ponto de partida
from geopy import Nominatim, distance
import pycep_correios

cep1 = int(input('Digite o CEP do endereço de partida: '))
    
endereco1 = pycep_correios.get_address_from_cep(cep1)

geolocator = Nominatim(user_agent="geolocalização") # coloque o nome do seu projeto em "user_agent"
print(f"{endereco1['logradouro'][0]}., {endereco1['bairro']} - {endereco1['cidade']}")

# Formato: R.  Capote Valente
rua = f"{endereco1['logradouro'][0]}. {endereco1['logradouro'][3:]}"
# Pinheiros
bairro = endereco1['bairro']
# São Paulo
cidade = endereco1['cidade']

localizacao = geolocator.geocode(f"{rua}, {bairro}-{cidade}")

print((localizacao.latitude, localizacao.longitude))




#função que calcula os km entre o ponto de partida e o destino
