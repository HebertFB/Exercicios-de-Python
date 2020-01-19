# EX22
print('\033[1;33m=-\033[m' * 33)
print(f'{" " * 18} \033[1;33mVerificação de aprosentadoria:\033[m')
print('\033[1;33m=-\033[m' * 33)
idade = input(f'\n {" " * 23} \033[1;96mInforme sua idade: \033[m')

if idade >= '65':
    print('\nTrabalhador ter 65 anos de idade ou mais!')
    print(f'\033[1;92mO trabalhador tem {idade} anos, portanto tem resquisito válido para se aposentar!\033[m')
else:
    if idade < '45':
        print('\n\033[1;31mNão está apto á aposentadoria!!!\033[m')
    else:
        tempo_servico = input(f' {" " * 19} \033[1;96mInforme o tempo (anos) de serviço: \033[m')
        if tempo_servico >= '30':

            print('\nTrabalhado ter trabalhado 30 anos ou mais!')
            print(f'\033[1;92mO trabalhador tem {tempo_servico} anos de contribuição,'
                  f' portanto tem resquisito válido para se aposentar!\033[m')

        elif idade >= '60' and tempo_servico >= '25':
            print('\nTrabalhado ter pelo menos 60 anos de idade e pelo men  os 25 anos trabalhados!')
            print(f'\033[1;92mO trabalhador tem {idade} anos de idade e {tempo_servico} anos de contribuição'
                  f'\nPortanto tem resquisito válido para se aposentar!\033[m')

        else:
            print('\n\033[1;31mNão está apto á aposentadoria!!!\033[m')
