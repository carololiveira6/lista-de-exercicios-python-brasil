"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 galão(ões) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 galão(ões) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""

import sys
import math

def calcular_latas_e_preco_de_tinta():
    area = float(input('Digite o tamanho, em metros quadrados, da área a ser pintada: '))
    cobertura_por_litro = 6 # 1 * 6.0
    lata_de_tinta = 18
    preco_da_lata = 80
    galoes_de_tinta = 3.6
    preco_do_galao = 25
    folga = 0.10
    
    area_com_folga = area * (1 + folga)
    litros_necessarios = math.ceil(area_com_folga / cobertura_por_litro)

    latas_necessarias = math.ceil(litros_necessarios / lata_de_tinta)
    preco_total_latas = latas_necessarias * preco_da_lata
    sobra_litros_latas = (latas_necessarias * lata_de_tinta) - litros_necessarios

    galoes_necessarios = math.ceil(litros_necessarios / galoes_de_tinta)
    preco_total_galoes = galoes_necessarios * preco_do_galao
    sobra_litros_galoes = (galoes_necessarios * galoes_de_tinta) - litros_necessarios

    latas_mix = litros_necessarios // lata_de_tinta # divisão inteira
    litros_restantes = litros_necessarios % lata_de_tinta # resto da divisão
    galoes_mix = math.ceil(litros_restantes / galoes_de_tinta)

    if galoes_mix * preco_do_galao > preco_da_lata:
        latas_mix += 1
        galoes_mix = 0

    preco_total_mix = (latas_mix * preco_da_lata) + (galoes_mix * preco_do_galao)
    sobra_litros_mix = (latas_mix * lata_de_tinta) + (galoes_mix * galoes_de_tinta) - litros_necessarios

    print(f'Você deve comprar {litros_necessarios} litro(s) de tinta.')
    print(f'Você pode comprar {latas_necessarias} lata(s) de 18 litros a um custo de R$ {preco_total_latas}. '
          f'Vão sobrar {sobra_litros_latas:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {galoes_necessarios} galão(ões) de 3.6 litros a um custo de R$ {preco_total_galoes}. '
            f'Vão sobrar {sobra_litros_galoes:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {latas_mix} lata(s) de 18 litros e {galoes_mix} galão(ões) de 3.6 litros '
            f'a um custo de R$ {preco_total_mix}. Vão sobrar {sobra_litros_mix:.1f} litro(s) de tinta.')
    
    
    sys.exit(0)

calcular_latas_e_preco_de_tinta()