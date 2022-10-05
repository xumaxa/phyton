matriz = [[1,2],[3,4]]

def intr_matriz(fila,col):
    matriz=[]
    for i in range(fila):
        a=[0]*col
        matriz.append(a)
    for i in range(fila):
        for c in range(col):
            matriz[i][c]=input("Elemento:")
    return matriz
def zoom(matriz):
    for i in range(len(matriz[0])):
        for c in range(len(matriz)):
            matriz[i][c] = 
