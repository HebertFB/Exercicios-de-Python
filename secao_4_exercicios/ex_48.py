# Exercicio 48
segundos = int(input('informe os segundos: '))

segfinal = segundos % 86400
horas = segfinal // 3600
segfinal = segfinal % 3600
minutos = segfinal // 60
segfinal = segfinal % 60

print(f'\nSão {horas:.0f} horas {minutos:.0f} minutos e {segfinal:.0f} segundos.')

