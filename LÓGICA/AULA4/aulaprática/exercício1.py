
print("Bem vindo a nossa lanchonete!")
print("Escolha uma opção:")
print("1 - Coxinha")
print("2 - Pastel")
print("3 - Café")
print("4 - Suco")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print("Você escolheu Coxinha. O valor é R$ 5,00")
elif opcao == 2:
    print("Você escolheu Pastel. O valor é R$ 7,00")
elif opcao == 3:    
    print(" Vocé escolheu Café. O valor é R$ 4,00")
elif opcao == 4:
    print(" Vocé escolheu Suco. O valor é R$ 6,00")
else:
    print("Opção inválida.")