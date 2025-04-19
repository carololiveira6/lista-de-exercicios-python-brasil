"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) de tinta ao custo de R$ 160.00


"""

import sys
import math

def calcular_latas_e_preco_de_tinta():
    area = float(input('Digite o tamanho, em metros quadrados, da área a ser pintada: '))
    cobertura_por_litro = 3.0 # 1 * 3.0
    lata_de_tinta = 18.0
    preco_da_lata = 80.00

    cobertura_por_lata = lata_de_tinta * cobertura_por_litro # 54

    latas_necessarias = math.ceil(area / cobertura_por_lata)

    preco_total = latas_necessarias * preco_da_lata
    
    print(f'Você deve comprar {latas_necessarias} lata(s) de tinta ao custo de R$ {preco_total:.2f}')

    sys.exit(0)

calcular_latas_e_preco_de_tinta()