nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if nome == "Vinicius":
    print("Olá, Vinicius.")

elif idade < 18:
    print("Você é menor de idade.")
elif idade > 100:
    print("Esta pessoa provavelmente não existe.")