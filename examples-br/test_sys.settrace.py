def trace(frame, event, arg_unused):
    print(f"{event}\t{frame.f_lineno}\t{frame.f_locals}")
    return trace

def gerar_gabarito(maximo, contador, soma):
    while contador <= maximo:
        if contador % 2 == 0:  # Adicionar operador de igualdade para verificar se é par
            soma += contador  # Incrementar o valor de soma com o contador
        else:
            soma -= contador  # Incrementar o valor de soma com o contador
        contador += 1  # Incrementar o contador

import sys
sys.settrace(trace)
resultado = gerar_gabarito(9, 7, 6)
sys.settrace(None)

