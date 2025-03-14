"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    >>> from secao_01_estrutura_sequencial import ex_05_metros_para_centimetros
    >>> ex_05_metros_para_centimetros.input = lambda k: '1'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 100.0 cm
    >>> ex_05_metros_para_centimetros.input = lambda k: '3.621'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 362.1 cm

"""
import sys

def converter_metros_para_centimetros():
  tamanho = float(input('Digite o tamanho, em metros, a ser convertido: '))
  converter = tamanho * 100
  print(f'Transformando {tamanho}m para centímetros, dá {converter}cm.')
  sys.exit(0)

converter_metros_para_centimetros()