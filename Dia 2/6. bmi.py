peso = input("Informe o peso:")
altura = input("Informe a altura:")
print(type(altura))
print(type(peso))
imc = float(peso) / float(altura)**2
print("Seu IMC é: " + str(imc))
