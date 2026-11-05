print('Calculadora de consumo de energia elétrica')
print('Qual a quantidade de energia consumida em kWh?')
kwh = float(input())

print('Qual o tipo de instalação?')
print('1. Residencial')
print('2. Comercial')
print('3. Industrial')
tipo = int(input())

if (tipo == 1):
    if (kwh <= 500):
        valor = kwh * 0.40
        print(f'O valor a pagar é: R$ {valor:.2f}')
    else:
        valor = kwh * 0.65
        print(f'O valor a pagar é: R$ {valor:.2f}')

elif (tipo == 2):
    if (kwh <= 1000):
        valor = kwh * 0.55
        print(f'O valor a pagar é: R$ {valor:.2f}')
    else:
        valor = kwh * 0.60
        print(f'O valor a pagar é: R$ {valor:.2f}')

elif (tipo == 3):
    if (kwh <= 5000):
        valor = kwh * 0.55
        print(f'O valor a pagar é: R$ {valor:.2f}')
    else:
        valor = kwh * 0.60
        print(f'O valor a pagar é: R$ {valor:.2f}')

else:
    print('Opção inválida.')


