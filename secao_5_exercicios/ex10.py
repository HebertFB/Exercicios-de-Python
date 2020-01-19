# EX10
print('\033[1;93mUTILIZE PONTO NO LUGAR DA VÍRGULA PARA INFORMAR AS NOTAS!\033[m')
altura = float(input('Informe sua altura: '))
sexo = str(input('Informe seu sexo: '))

if sexo.lower() == 'homem' or sexo.lower() == 'h':
    print(f'\nO peso ideal para você é {(72.7 * altura) - 58:.2f} kilos!')
elif sexo.lower() == 'mulher' or sexo.lower() == 'm':
    print(f'\nO peso ideal para você é {(62.1 * altura) - 44.7:.2f} kilos!')

