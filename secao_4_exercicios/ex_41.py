# Exercicio 41
valor = float(input('Informe o valor da hora trabalhada (Obs: Utilize ponto no lugar da vírgula): R$ '))
horas = int(input('Informe o nùmero de horas trabalhadas no mês: '))

print(f'\nPara {horas} hora(s) trabalhada(s), o valor a ser pago com 10% de acréscimo no total é de R$ {(valor * horas) * 1.10:.2f}')

