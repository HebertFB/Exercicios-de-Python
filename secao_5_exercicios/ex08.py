# Ex08
print('\033[1;93mUTILIZE PONTO NO LUGAR DA VÍRGULA PARA INFORMAR AS NOTAS!\033[m')
nota1 = float(input('\nInforme a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

if nota1 < 0.0 or nota1 > 10.0:
    print('\n\033[1;91mA 1° nota informada e inválida!!!\033[m')
elif nota2 < 0.0 or nota2 > 10.0:
    print('\n\033[1;91mA 2° nota informada e inválida!!!\033[m')
else:
    print(f'\n\033[1;94mA média do aluno é {(nota1 + nota2) / 2:.2f}!\033[m')

