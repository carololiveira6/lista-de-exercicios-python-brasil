"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato ( 5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""

import sys

def calcular_assalto_no_salario():
    horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))
    valor_hora = float(input('Digite o valor ganho por hora trabalhada: '))

    salario_bruto = horas_trabalhadas * valor_hora

    desconto_ir = salario_bruto * 0.11
    desconto_inss = salario_bruto * 0.08
    desconto_sindicato = salario_bruto * 0.05

    descontos = desconto_ir + desconto_inss + desconto_sindicato

    salario_liquido = salario_bruto - descontos

    print(f'+ Salário Bruto: R$ {salario_bruto:.2f}')
    print(f'- IR (11%): R$ {desconto_ir:.2f}')
    print(f'- INSS (8%): R$ {desconto_inss:.2f}')
    print(f'- Sindicato (5%): R$ {desconto_sindicato:.2f}')
    print(f'= Salário Líquido: R$ {salario_liquido:.2f}')

    sys.exit(0)

calcular_assalto_no_salario()