lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))

if (lado1 > 0) and (lado2 > 0) and (lado3 > 0) and (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo.")

else:
    print("Os lados não formam um triângulo.")

if (lado1 == lado2) and (lado2 == lado3):
    print("O triângulo é equilátero.")

elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print("O triângulo é isósceles.")

else:
    print("O triângulo é escaleno.")