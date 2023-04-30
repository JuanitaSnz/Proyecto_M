
def coeficientes_matriz(n, m):
    matriz = []
    print('-----Ingreso de los coeficientes de las variables-----')
    for i in range(0,n):
        matriz.append([])
        for j in range(0,m):
            matriz[i].append(float(input('Ingrese valor['+str(i)+']['+str(j)+']: ')))
    return matriz

def coeficientes_indepentiendes(n):
    out = []
    print('-----Ingreso de los coeficientes independientes-----')
    for i in range(0,n):
        out.append(float(input('Ingrese valor [' + str(i) + ']: ')))
    return out


def valores_inicial(n):
    out = []
    print('-----Ingreso de los coeficientes independientes-----')
    for i in range(0,n):
        out.append(float(input('Ingrese valor [' + str(i) + ']: ')))
    return out


n = int(input('Ingrese numero de filas (n): '))
m = int(input('Ingrese numero decolumnas (m): '))
# [[4,-1,0,0],[-1,4,-1,0],[0,-1,4,-1],[0,0,-1,4]]
# [1,1,1,1]
A = coeficientes_matriz(n, m)
b = coeficientes_indepentiendes(n)
x0=valores_inicial(n)
k=0
norma = 1
error=float(input("Ingrese el error"))
max_iteraciones=int(input("Ingrese el numero de iteraciones maximo"))
cont = 0
infinity = float('inf')

while norma > error:
    k += 1
    x = []
    for i in range(0,3):
        suma = 0
        for j in range(0,3):
            if i != j:
                suma += A[i][j]*x0[j]
        x.append((b[i]-suma)/(A[i][i]))
        b[i]=x[i]
        if x[i] == float('inf'):
            cont = 1

    norma = abs(x0[0]-x[0])

    print("\nEl vector en la iteracion "+str(k)+" es igual: \n" +str(x))

    x0 = x
    if k > max_iteraciones:
        print('\nNo se alcanzo la convergencia')
        break
