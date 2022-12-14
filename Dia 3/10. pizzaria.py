print("Bem vindo a Pizzaria")

tam = input("Qual o Tamanho do Pizza? (P / M / G)")
pepe = input("Deseja peperoni? (S / N)")
queijo = input("Queijo extra? (S / N)")

preco = 0

if tam == "P":
    preco = 15
elif tam == "M":
    preco = 20
elif tam == "G":
    preco = 25

if queijo == "S":
    preco +=1

if pepe == "S":
    if tam == "P":
        preco += 2
    else:
        preco += 3

print(f"O total da conta é {preco}")