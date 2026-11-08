# Exercício 4:
# Um cinema cobra preços diferentes para os ingressos de acordo com a idade da pessoa.
# Se tiver menos de 3 anos, o ingresso será gratuito.
# Se tiver entre 3 e 12 anos, o ingresso custará R$ 15.
# Se tiver mais de 12 anos, o ingresso custará R$ 30.
#
# Complemento:
# Escreva um laço que pergunte a idade aos usuários e informe o preço do ingresso.
# Encerre o laço usando break quando o usuário digitar zero.
# Após encerrar o laço, apresente:
# - O total de pessoas que compraram ingressos.
# - O total de dinheiro arrecadado.
# - A média de idade das pessoas.

idade = int(input("Digite sua idade: "))

total_pessoas = 0
total_arrecadado = 0
media_idade = 0

while idade != 0:
    if idade < 3:
        print("Ingresso gratuito.")
    elif 3 <= idade <= 12:
        print("Ingresso custa R$ 15.")
        total_arrecadado += 15
    else:
        print("Ingresso custa R$ 30.")
        total_arrecadado += 30

    total_pessoas += 1
    media_idade += idade

    idade = int(input("Digite sua idade (ou 0 para encerrar): "))

media_idade /= total_pessoas

print("Total de pessoas que compraram ingressos:", total_pessoas)
print("Total de dinheiro arrecadado:", total_arrecadado)
print("Média de idade das pessoas:", media_idade)

print("Obrigado por utilizar nosso sistema de venda de ingressos!")