# Exercicio 30
reais = float(input('Informe o valor em Reais a ser convertido, Obs: utilize ponto no lugar do vírgula: R$'))
cotacao = float(input('Informe a contação atual do Dolar a ser convertido: $'))

print(f'\nO valor de R${reais} em dolares é de aproximadamente ${reais / cotacao:.2f}')

