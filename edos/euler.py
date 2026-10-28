import numpy as np



def euler(fun,tempos,y0):
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
        y.append(y[-1] + fun(t,y[-1]) * dt)

    return np.array(y)
