#ano bissexto
year = int(input("Digite um ano: "))

valid=False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          valid=True  

if valid == True:
    print(f"{year} é um ano bissexto")
else:
    print(f"{year} não é um ano bissexto!")