"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    notas = []

    nota_1 = float(input("Digite a primeira nota: "))
    notas.append(nota_1)

    nota_2 = float(input("Digite a segunda nota: "))
    notas.append(nota_2)

    nota_3 = float(input("Digite a terceira nota: "))
    notas.append(nota_3)

    nota_4 = float(input("Digite a quarta nota: "))
    notas.append(nota_4)

    media = sum(notas) / len(notas)

    print("A média anual é", media)

calcular_media()