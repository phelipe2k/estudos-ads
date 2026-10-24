# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto

preco = float(input("Digite o preco do produto: "))
desconto = float(input("Digite o percentual de desconto (0 a 100%): "))

desconto = preco * (desconto / 100)
preco_final = preco - desconto

print(f"O preco do produto era de R${preco:.2f}")
print(f"O desconto é de R${desconto:.2f}")
print(f"O preco final é de R${preco_final:.2f}")

