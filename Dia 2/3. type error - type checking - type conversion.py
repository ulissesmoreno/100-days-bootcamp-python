num_char = len(input("Qual o seu nome?"))
#print("Seu nome tem: " + num_char + " letras.")

#Ao usarmos esse código obtemos o seguinte erro:
#TypeError: can only concatenate str (not "int") to str
#A funcionalidade de concatenar apenas funciona com strings, e a variável é um integer

print(type(num_char))
#Função type mostra o tipo de dados da variável.

print(type(len(input("Qual o seu nome?"))))
#Mesmos passos anteriores, porém em uma única linha

new_num_char = str(num_char)
print("Seu nome tem: " + new_num_char + " letras.")
print("Seu nome tem: " + str(num_char) + " letras.")

#Usando o comando str para covnerter para string

a = 123
print(type(a))

a=str(a)
print(type(a))

a=float(a)
print(type(a))

print(70 + float("100.5"))

print(str(70) + float("100.5"))

#Outras conversões