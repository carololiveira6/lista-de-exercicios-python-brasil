"""
Exercício 06 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Mostrar a área com 4 casas decimais.
Observação: Use o valor de 3.1415 para o valor da constante π

    >>> from secao_01_estrutura_sequencial import ex_06_area_circulo
    >>> ex_06_area_circulo.input = lambda k: '1'
    >>> ex_06_area_circulo.calcular_area_de_circulo()
    A área do círculo com esse raio é: 3.1415
    >>> ex_06_area_circulo.input = lambda k: '2.5'
    >>> ex_06_area_circulo.calcular_area_de_circulo()
    A área do círculo com esse raio é: 19.6344

"""
import sys

def calcular_area_de_circulo():
    raio = float(input('Digite o raio do círculo: '))
    area = 3.1415 * (raio ** 2)
    print(f'A área do círculo é: {area: .4f}')
    sys.exit(0)

calcular_area_de_circulo()
