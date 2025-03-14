"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça dois números inteiros e imprima a soma.

    >>> from secao_01_estrutura_sequencial import ex_03_imprima_soma_de_dois_numeros
    >>> numeros =['42', '43']
    >>> ex_03_imprima_soma_de_dois_numeros.input = lambda k: numeros.pop()
    >>> ex_03_imprima_soma_de_dois_numeros.imprima_a_soma_de_dois_numeros()
    A soma dos dois números informados é 85

"""
import sys

def imprima_a_soma_de_dois_numeros():
    first_number = int(input("Digite o primeiro número: "))
    second_number = int(input("Digite o segundo número: "))
    result = first_number + second_number
    print("A soma dos dois números informados é", result)
    sys.exit(0)

imprima_a_soma_de_dois_numeros()
