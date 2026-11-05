print('Calculadora')
print('Escolha uma opção:')
print('1. Adição +')
print('2. Subtração -')
print('3. Multiplicação *')
print('4. Divisão /')

opcao = int(input('Digite a opção desejada: '))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))   

if (opcao == 1):
    resultado = n1 + n2
    print(f'O resultado da adição é: {resultado}')
elif (opcao == 2):
    resultado = n1 - n2
    print(f'O resultado da subtração é: {resultado}')
elif (opcao == 3):
    resultado = n1 * n2
    print(f'O resultado da multiplicação é: {resultado}')
elif (opcao == 4):
    resultado = n1 / n2
    print(f'O resultado da divisão é: {resultado}')
else:
    print('Opção inválida.')