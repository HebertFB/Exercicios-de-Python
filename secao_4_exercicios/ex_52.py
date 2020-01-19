# Exercício 52
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul_bebe':'\033[0;36m',
         'verde':'\033[1;32m'}
print(f"{cores['azul_bebe']}=-{cores['azul_bebe']}" * 30)
premio = float(input(f"{cores['limpa']}Informe o valor do prêmio: R$"))
apostador1 = float(input('\nDigite o valor investido pelo 1° apostador: R$'))
apostador2 = float(input('Digite o valor investido pelo 2° apostador: R$'))
apostador3 = float(input('Digite o valor investido pelo 3° apostador: R$'))
print(f"{cores['azul_bebe']}=-{cores['azul_bebe']}" * 30)

aposta_total = apostador1 + apostador2 + apostador3
valor_ap1 = aposta_total / apostador1
valor_ap2 = aposta_total / apostador2
valor_ap3 = aposta_total / apostador3
print(f"{cores['amarelo']}=-{cores['amarelo']}" * 30)
print(' '*20 + f'PRÊMIO NO VALOR DE R${premio:.2f}')
print(f"{cores['amarelo']}=-{cores['amarelo']}" * 30)
print(f"\n{cores['azul_bebe']} 1° Ganhador apostou {cores['verde']}R${apostador1:.2f}{cores['azul_bebe']} e receberá {cores['amarelo']}R${premio / valor_ap1:.2f}")
print(f"{cores['azul_bebe']} 2° Ganhador apostou {cores['verde']}R${apostador2:.2f}{cores['azul_bebe']} e receberá {cores['amarelo']}R${premio / valor_ap2:.2f}")
print(f"{cores['azul_bebe']} 3° Ganhador apostou {cores['verde']}R${apostador3:.2f}{cores['azul_bebe']} e receberá {cores['amarelo']}R${premio / valor_ap3:.2f}\n")

print('=-' * 30)

