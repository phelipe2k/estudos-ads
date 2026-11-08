##Escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuário, até que ele digite a palavra "sair".
##O algoritmo deve imprimir na tela todas as palavras digitadas, exceto a palavra "sair"

##Aprender a usar o break
##O comando break é usado para encerrar um loop antes que ele termine naturalmente. Ele é útil quando você deseja sair de um loop com base em uma condição específica.



print("Digite palavras ou frases. Digite 'sair' para encerrar o programa.")
while True:  # Loop infinito
    texto = input("Digite uma palavra ou frase: ")  # Solicita ao usuário que digite uma palavra ou frase
    print("Você digitou:", texto)  # Imprime a palavra ou frase digitada
    if texto == "sair":  # Se o usuário digitar "sair"
        print("Programa encerrado.")  # Imprime uma mensagem de encerramento
        break  # Encerra o loop
    else:
        continue