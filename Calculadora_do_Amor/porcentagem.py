import random

# valor conterá dígitos entre 0-9
porcentagem = '0123456789'

# resultado será em dois dígitos
digitos = 2

# variável temporária que obtém o resultado
resultado = "".join(random.sample(porcentagem, digitos))

# retornando o resultado
print(resultado)