print("Calculadora do amor")
nome1 = input("Qual o seu nome?\n")
nome2 = input("Qual o nome dela(e)?\n")

nomeambos = nome1.lower() + nome2.lower()

pontt = 0
pontt += nomeambos.count("t")
pontt += nomeambos.count("r")
pontt += nomeambos.count("u")
pontt += nomeambos.count("e")

pontl = 0
pontl += nomeambos.count("l")
pontl += nomeambos.count("o")
pontl += nomeambos.count("v")
pontl += nomeambos.count("e")

scores = str(pontt) + str(pontl)
scoref = int(scores)
print(type(scoref))

if scoref < 10 or scoref > 90:
    print(f"Sua pontuação final é {scoref}, você dão certo igual Coca e Mentos")
elif scoref >= 40 and scoref <= 50:
    print(f"Sua pontuação final é {scoref}, parabéns! Feitos um para o outro")
else:
    print(f"Sua pontuação final é {scoref}")