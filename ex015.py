#Exercício Python 15: Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('km percorrido : '))
dia = int(input('Dias alugados : '))
pago = (km * 0.15) + (dia * 60)
print('Total a pagar é R${:.2f}'.format(pago))
