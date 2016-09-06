#!/usr/env python
import sys

def achar_soma(sequencia):
    maximo = sequencia[0]
    max_comeco = max_final = 0
    S = sequencia[0]
    T = 0
    for i in range(1, len(sequencia)):
        if S > 0:
            S += sequencia[i]
        else:
            S = sequencia[i]
            T = i
        if S > maximo:
            max_comeco = T
            max_final = i
            maximo = S
    return max_comeco, max_final, maximo

def main():
    
    sequencia = [1, 2, 3, -4, 1]

    i, j, soma = achar_soma(sequencia)
    sub_sequencia = sequencia[i:j+1]
    print(soma, sub_sequencia)

main()
