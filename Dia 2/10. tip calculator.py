print("Bem vindo a calculadora de gorjetas")
valor_conta = input("Digite o valor da conta: ")
porcentagem = input("Qual a % da gorjeta? 10,12 ou 20: ")
pessoas = input("Quantas pessoas? ")

resultado = round(float(valor_conta) / int(pessoas) * (float(porcentagem) / 100 +1),2)

print(f"O valor por pessoa é {resultado}")
