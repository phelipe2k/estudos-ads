##Escreva um algoritmo que realize um login em um sistema
##O usuário deve informar seu nome e senha

##Aprender a usar o continue
##O comando continue é usado para pular a iteração atual de um loop e passar para
##a próxima iteração. Ele é útil quando você deseja ignorar certas condições e continuar com o loop.


print("Bem-vindo ao sistema de login.")
while True:  # Loop infinito
    nome = input("Digite seu nome: ")  # Solicita ao usuário que digite seu nome
    if (nome != "admin"):  # Se o nome digitado não for "admin"
        print("Nome de usuário inválido. Tente novamente.")  # Imprime uma mensagem de erro
        continue  # Pula para a próxima iteração do loop
    senha = input("Digite sua senha: ")  # Solicita ao usuário que digite sua senha
    if (senha != "123"):  # Se a senha digitada não for "123"
        print("Senha inválida. Tente novamente.")  # Imprime uma mensagem de erro
        continue  # Pula para a próxima iteração do loop
    print("Login bem-sucedido.")  # Imprime uma mensagem de sucesso
    break  # Encerra o loop