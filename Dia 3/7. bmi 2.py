peso = input("Informe o peso:")
altura = input("Informe a altura:")
print(type(altura))
print(type(peso))
imc = float(peso) / float(altura)**2
imc = round(imc,2)
print(f"Seu IMC é: {imc}")
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Você tem o peso normal")
elif imc < 30:
    print("Você está com sobrepeso")
elif imc < 35:
    print("Você está obeso")
else:
    print("Obesidade mórbida")