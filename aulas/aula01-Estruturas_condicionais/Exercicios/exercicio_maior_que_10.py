import os
os.system("cls")

#Elabore um algoritmo para solicitar ao usuário um valor e escreva a mensagem: É MAIOR QUE 10
#Se o valor lido for maior que 10, caso contrário: NÃO É MAIOR QUE 10

numero1 = int(input("Me informe um numero: "))

if numero1 > 10:
    print ("É MAIOR QUE 10")
elif numero1 < 10:
    print("É MENOR QUE 10")
    
    print("Fim")