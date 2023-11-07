#contador
carneiros = 0

while True: #enquanto for verdadeiro
    resp = input('Já dormiu?')
    if resp == 's' or resp == "S":
        break #paran a estrutura de repetição
    else:
        carneiros = carneiros + 1

print(carneiros)