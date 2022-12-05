print(8/3)

print(round(8/3,2))
#Para arredondar usar função round()

print(8 // 3)
#Trás a parte interira da divisão

print(type(8 // 3))
#Até o tipo é int

result = 4/2
result /= 2
#Esse comando divide o valor da variável por 2

print(result)

score=0
score +=1
print("Sua potuação é: " + str(score))
#Usando o função STR

#f-String
print(f"Sua potuação é: {score}")
#permite colocar variáveis dentro de string, sem a necessidade das conversões

height = 1.8
isWinning = True

print(f"Sua pontução é {score}, sua altura é {height} e você está ganhando? {isWinning}!")