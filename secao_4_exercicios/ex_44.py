# Exercicio 44
import math
degrau = float(input('Informe a altura do degrau, Obs: utilize ponto no lugar da vírgula: '))
altura = float(input('\nInforme a altura que deseja alcançar subindo a escada, Obs: utilize ponto no lugar da vírgula: '))

print(f'Vaoçê terá de subir {math.ceil((altura*100)/degrau)} degraus para alcançar {altura}.')

