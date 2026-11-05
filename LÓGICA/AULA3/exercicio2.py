print('Escolha uma opção:')
print('1. maçã')
print('2. banana')
print('3. laranja')

produto = int(input('Digite o número do produto desejado: '))
qtd = int(input('Digite a quantidade desejada: '))

if (produto == 1):
    pagar = qtd * 2.3
    print(f'Você escolheu {qtd} maçãs, Total: R$ {pagar:.2f}.')
elif (produto == 2):
    pagar = qtd * 1.85
    print(f'Você escolheu {qtd} bananas, Total: R$ {pagar:.2f}.')
elif (produto == 3):
    pagar = qtd * 3.6
    print(f'Você escolheu {qtd} laranjas, Total: R$ {pagar:.2f}.')
else:
    print('Opção inválida.')