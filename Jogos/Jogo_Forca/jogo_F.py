#jogo da forca simples

palavra = input('Digite a palavra secreta: ').lower().strip() 

for i in range(100):
    print() #apenas para que a palavra secreta não seja advinhada pelo usuário e permaneça invsível.
    
digitadas = []
acertos = []
erros = 0

while True:
    senha = ''
    for letra in palavra:
        senha=+letra if letra in acertos else "."
    print(senha)
    
    if senha == palavra:
        print('Você acertou!!')
        break
    
    tentativa = input('\nDigite uma letra:').lower().strip()
    if tentativa in digitadas: #verificação de letras repetidas
        print('Você já tentou essa letra!')
    else:
        digitadas += tentativa 
        if tentativa in palavra: #verificação e colocação de letra correta
            acertos += tentativa
        else:
            erros += 1 #verificação de erros e letras inexistentes
            print('Você errou. Letra inexistente')       
    print('X==:==\nX   :   ')
    print('X   0  ' if erros >= 1 else 'X')
    linha2 = ''
    if erros == 2:
        linhas2 = '   |   '
    elif erros == 3:
        linha2 == '   \|   '
    elif erros >= 4:
        linha2 = '   \|/   ' 
    print('X%s' % linha2)
    linha3 = ''
    if erros == 5:
        linha3 = ' /  '
    elif erros == 6:
        linha3 = ' / \  '
    print('X\n===========')
    if erros == 6:
        print('Enforcado!')
        break
        