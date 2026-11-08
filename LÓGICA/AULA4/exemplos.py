##Crie um algoritmo que receba um valor do tipo inteiro via teclado
##No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos
##Qualquer valor negativo, ou igual a zero, deve ser rejeitato pelo programa, e um novo valor deve ser solicitado ao usuário, até que um valor válido seja digitado.




x = -1  # Inicializa x com um valor inválido
while x <= 0:  # Enquanto x for menor ou igual a zero
    x = int(input("Digite um valor inteiro e positivo: ")) ##Solicita ao usuário que digite um valor inteiro e positivo
    if x <= 0: ##Se x for menor ou igual a zero
        print("Valor inválido. Por favor, digite um valor inteiro e positivo.") ##Se x for menor ou igual a zero, exibe uma mensagem de erro
    

print("O valor digitado foi:", x) ##Imprime o valor digitado


    