if __name__ == '__main__':
    x = int(input())  #linha
    y = int(input())  #colunas
    n = int(input())

    matriz=[]
    for i in range(x+1):
        for j in range(y+1):
            if i+j==n:
                continue
            else:
                matriz.append([i,j])
    
print(matriz)

#    z = int(input())
#    
#