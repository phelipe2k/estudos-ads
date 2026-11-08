print("Bem-vindo ao sistema de contagem de cedulas!")
valor = int(input("Digite o valor a ser sacado: "))

cedulas = [100, 50, 20, 10, 5, 2, 1]
total_cedulas = 0

for cedulas in cedulas:
    total_cedulas += valor // cedulas
    valor %= cedulas

print("O total de cedulas a serem entregues é:", total_cedulas)