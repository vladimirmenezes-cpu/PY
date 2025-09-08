import os
os.system("cls")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo  valor: "))
c = 0

if a == b:
   c = a + b
   print( "Os valores são iguais. A soma é: {c}")
else:
    c = a * b
print( "Os valores são diferentes. A multiplicação é: {c}")