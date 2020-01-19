# EX09
print('\033[1;93mUTILIZE PONTO NO LUGAR DA VÍRGULA PARA INFORMAR AS NOTAS!\033[m')
salario = float(input('\nInforme seu salário: '))
emprestimo = float(input('Informe o valor da prestação do empréstimo: '))

porcetagem = salario * (20 / 100)

if emprestimo > porcetagem:
    print(f'\n\033[1;91mEmpréstimo não concedido!!!\033[m')
else:
    print(f'\n\033[1;94mEmpréstimo concedido!!!\033[m')

