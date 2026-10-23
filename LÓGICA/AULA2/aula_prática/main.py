# Exércicios de fixação
# Escreva as seguintes expressôes algébricas em linguagem Python:
#.A O Somatório dos 5 primeiros números inteiros e positivos
#.B A média entre 23, 19 e 31
#.C O número de vezes que 73 cabe em 403
#.D A sobra quando 403 é dividido por 73

print(1+2+3+4+5)

print((23+19+31)/3)

print(403//73)

print(403%73)

# Escreva as seguintes expressões algébricas em linguagem Python:
    #E. 2 elevado à 10ª potência
    #F. O valor absoluto da diferença entre 54 e 57
    #G. O menor valor entre 34, 29 e 31

print(2**10)

print(abs(54-57))

print(min(34,29,31)) 

# Escreva as expressões em Python para: 
    #H. Atribuir o valor inteiro 3 à variável a
    #I. Atribuir o valor 4 à variável b
    #J. Atribuir à variável c o valor da expressão a*a + b*b


a = 3
b = 4
c = a*a + b*b

print(f"O resultado da expressão é {c}") 

# Execute as seguinte atribuições:
    #K. s1 = 'ant'
    #L. s2 = 'bat'
    #M. s3 = 'cod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'


# Agora, utilizando operadores + e *, crie as saídas a seguir:

   #a. 'ant bat cod'
   #b. 'ant ant ant ant ant ant ant ant ant ant'
   #c. 'ant bat bat cod cod cod'
   #d. 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat
   #e. 'batbatcod batbatcod batbatcod batbatcod batbatcod

res = s1 + ' ' + s2 + ' ' + s3
print(res)

res = (s1 + ' ') * 10
print(res)

res = (s1+ ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print(res)

res = (s1 + ' ' + s2 + ' ') * 7
print(res)

res = (s2 + s2 + s3 + ' ') * 6
print(res)
