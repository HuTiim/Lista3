import numpy as np

def rk4(fun,tempos,y0):

    '''
    Método de Euler para resolver dy/dt = f(t, y) com condição inicial y0.
    As soluções são calculadas nos instantes de tempo t_eval. Aqui y e o
    retorno da função f(t, y) devem ser compatíveis: ambos devem ser 
    escalares, ou ambos devem ser arrays do mesmo formato.
    INPUT
        fun (callable): Função f(t, y) que define a EDO.
        y0 (float ou array): Condição inicial.
        t_eval (iterable): Instantes de tempo nos quais a solução será calculada.
    OUTPUT
        y (array): Valores aproximados da solução nos instantes de t_eval.
    '''

    y = [y0]
    dt = tempos[1] - tempos[0]

    for t in tempos[:-1]:

        k1 = fun(t, y[-1])
        k2 = fun(t + dt/2, y[-1] + k1*dt/2)
        k3 = fun(t + dt/2, y[-1] + k2*dt/2)
        k4 = fun(t + dt , y[-1] + dt*k3)

        y.append(y[-1] + dt/6 * (k1 + 2*k2 + 2*k3 + k4))

    return np.array(y)

