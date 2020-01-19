# EX02
print('De 1 à 100 com FOR:')
for n in range(1,101):
    print(n, end=' ')

print('\n\nDe 1 à 100 com WHILE:')
num = 0
while num < 100:
    num += 1
    print(num, end=' ')

print('\n\nDe 1 à 100 com "DO WHILE":')
numero = 1
while True:
    if numero == 101:
        break
    print(numero, end=' ')
    numero += 1

