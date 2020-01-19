# Exercício 53
comprimento = float(input('Digite o comprimento do terreno: '))

largura = float(input('Digite a largura do terreno: '))
cerca = (comprimento**2) + (largura**2)

tela = float(input('Informe o preço do metro da tela: '))

print(f'Custara R$ {cerca / tela:.2f} pra cercar o terreno. ')

