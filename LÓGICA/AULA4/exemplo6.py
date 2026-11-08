##Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o laço usando for

soma = 0
qtd = 0

for i in range(1, 101): # loop de 1 a 100
    if i % 2 == 0: # verifica se o número é par
        soma += i # adiciona o número à soma
        qtd += 1 # incrementa a quantidade de números pares

media = soma / qtd # calcula a média dos números pares

print(f"A média dos números pares de 1 até 100 é: {media:.2f}")