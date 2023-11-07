import json

with open('enderecos.json', 'r') as enderecos:
    todos_enderecos = json.load(enderecos)
    print(todos_enderecos)
