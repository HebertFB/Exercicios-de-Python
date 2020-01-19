# EX26
km = float(input("Informe os Km's percorridos: "))
litros = float(input("Informe os litros de combustivel consumidos: "))
print('\nCONSUMO  |  (Km/l)  |  MENSAGEM')

consumo = km / litros

if consumo < 8:
    print(f'menor que|    8     |  Venda o carro!'
          f'\n\n{consumo:.2f}')
elif consumo > 8 or consumo < 14:
    print(f'entre    |  8 e 14  |  Econômico!'
          f'\n\n{consumo:.2f}')
elif consumo > 12:
    print(f'maior que  |  8  |  Super econômico!'
          f'\n\n{consumo:.2f}')

