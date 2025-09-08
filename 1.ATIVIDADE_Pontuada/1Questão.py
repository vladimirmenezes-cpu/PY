import os
os.system("cls")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo  valor: "))
c = int(input("Digite o terceiro  valor: "))

soma = a + b

if soma < c:
    print("Soma do primeiro + segundo numero  é menor que o terceiro numero! ")
else:
    print("Soma do primeiro + segundo numero é maior que o terceiro numero! ")