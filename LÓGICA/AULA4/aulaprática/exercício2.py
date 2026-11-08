#Faça um algoritmo em que você seleciona o produto que quer comprar e a quantidade. Faça isso até que decida encerrar o programa. Ao final, mostre o valor final do pedido a ser pago.

print("Bem-vindo a lanchonete do Phelipe")
print("Escolha uma opção:")
print("1 - Coxinha")
print("2 - Pastel")
print("3 - Café")
print("4 - Suco")

valor_total = 0.00
while True:
    opcao = int(input("Digite a opção desejada (ou 0 para encerrar): "))

    if opcao == 0:
        break

    if opcao == 1:
        quantidade = int(input("Digite a quantidade de Coxinhas: "))
        valor_total += quantidade * 5.00
    elif opcao == 2:
        quantidade = int(input("Digite a quantidade de Pastéis: "))
        valor_total += quantidade * 7.00
    elif opcao == 3:
        quantidade = int(input("Digite a quantidade de Cafés: "))
        valor_total += quantidade * 4.00
    elif opcao == 4:
        quantidade = int(input("Digite a quantidade de Sucos: "))
        valor_total += quantidade * 6.00
    else:
        print("Opção inválida.")

print(f"O valor total do pedido é: R${valor_total:.2f}")