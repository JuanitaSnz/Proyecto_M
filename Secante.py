
import numpy as np
import matplotlib.pyplot as plt
# INGRESO
import sympy as sym

def secante(f,a,b,e):
    fx  = lambda x: eval(f)
    x = np.linspace(-10,10,1000);
    x0 =float(a)
    x1=float(b)
    error = float(e)
    # PROCEDIMIENTO
    tabla = []
    deltax = 0.002

    xi=x0

    while (error<deltax):
        xnuevo = xi - (fx(xi) * (xi - x1)) / (fx(xi) - fx(x1))
        deltax = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,deltax])
        xi = xnuevo
        #print('Deltax',deltax)

        # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    n = len(tabla)
    fi = fx(x)
    # SALIDA
    #print(['xi', 'xnuevo', 'deltax'])
    #np.set_printoptions(precision = 4)
    #print(tabla)
    #print('raiz en: ', xi)
    #print('con error de: ',deltax)
    if xi != np.nan:
        plt.axvline(xi)
    plt.plot(x,fi,label='f(x)')
    plt.axvline(0, color='k')
    plt.axhline(0, 0,color='k')
    plt.title('Secante')
    plt.legend()
    plt.plot(xi,0,'ro')
    return[plt.gcf(),xi,deltax,tabla]
