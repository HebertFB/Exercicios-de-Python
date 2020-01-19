# Exercicio 43
valorLido = float(input('Informe o valor do produto (Obs: Utilize ponto no lugar da vírgula): R$ '))

print('=-' * 40)
print(' ' * 30 + '*** CLIENTE ***')
print('=-' * 40)
desconto = valorLido * 0.90
print(f'O total a pagar com desconto de 10% é de R$ {desconto:.2f}')
print(f'O valor de cada parcela, no pagamento de 3x sem juros é de R$ {valorLido / 3:.2f}')

print('=-' * 40)
print(' ' * 30 + '*** VENDEDOR ***')
print('=-' * 40)
print(f'A comissão do vendedor, em caso de venda à vista é de R$ {desconto * 0.05:.2f}')
print(f'A comissão do vendedor, em caso de venda ser parcelada é de R$ {valorLido * 0.05:.2f}')

