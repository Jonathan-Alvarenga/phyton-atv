#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('primeiro segmento: '))
r2 = int(input('segundo segmento: '))
r3 = int(input('terceiro segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formam um triângulo!')
else:
    print('Não formam um triângulo!')