#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias
#pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input("Quantos dias alugados?"))
km = int(input("Quantos km rodados?"))

preco = (dias * 60) + (km * 0.15)


print(f'KM = {km}. Dias = {dias}')
print(f"O total a pagar é de R${preco:.2f}")