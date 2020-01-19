#Exercício 49
hora=int(input('Digite a hora: '))
min=int(input('Digite os minutos: '))
seg=int(input('Digite os segundos: '))

duracao=int(input('Digite a duração do experimento em segundos: '))

hora += (duracao / 3600)
aux = duracao
min += (aux / 60)
seg += duracao

print(f'O experimento acabará às {hora:.0f} horas {min:.0f} minutos {seg:.0f} segundos')

