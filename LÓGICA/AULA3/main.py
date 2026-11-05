print('Escolha uma opção:')
print('1. maçã')
print('2. banana')
print('3. laranja')

produto = int(input('Digite o número do produto desejado: '))
qtd = int(input('Digite a quantidade desejada: '))

if (produto == 1):
    print(f'Você escolheu {qtd} maçãs.')
    pagar = qtd * 2.3
    print(f'Valor a pagar: R$ {pagar:.2f}')
elif (produto == 2):
    print(f'Você escolheu {qtd} bananas.')
    pagar = qtd * 1.85
    print(f'Valor a pagar: R$ {pagar:.2f}')
elif (produto == 3):
    print(f'Você escolheu {qtd} laranjas.')
    pagar = qtd * 3.6
    print(f'Valor a pagar: R$ {pagar:.2f}')
else:
    print('Opção inválida.')