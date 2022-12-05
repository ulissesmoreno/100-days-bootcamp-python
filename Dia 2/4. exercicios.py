#Receber um valor com 2 digitos e somar ambos
num_digitado = input("Digite um número entre 10 e 99:")

num1 = str(num_digitado)[0]
num2 = str(num_digitado)[1]

resultado = int(num1) + int(num2)

print("A soma dos dois digitos digitados é:" + str(resultado))