#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('Digite um número e descubra se é par ou  ímpar :'))
resul = num % 2
if resul == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número é IMPAR!')




