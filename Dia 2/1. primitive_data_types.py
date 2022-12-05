print(len("Hello"))
#Ao usar a função LEN (comprimento de caracteres) o núemro retornado é a quantidade de caracteres na string

#print(len(12352))

#Porém ao usarmos essa mesma função com um número, obtemos um erro.
#TypeError: object of type 'int' has no len()
#Dados de tipo interiro não possuem comprimento, ou seja, não são cadeias de caracteres.
#O comando está comentado, pois sem isso, o código para.

#Data Types / Tipos de dados

#String
#Sequencia de caracteres, deve estar entre astas duplas ""

print("Hello"[0])
#Ao usar couchetes após a string podemos pegar apenas o caracter informado
#O primeiro item é o zero.

print("Hello"[4])
#Essa linha imprime o último carcter

print("Hello"[len("Hello")-1])

str_cumprimento = "Hello"
print(str_cumprimento[len(str_cumprimento)-1])
#Essa linha descobre "automaticamente" o último caracter da String e o imprime
#O -1 é necessário, pois, mesmo possuindo 5 caracters a contagem começa do zero, dessa forma são 5 caracters e a última posição é 4
#Funciona com variáveis também.

print("123" + "345")
#Se um número estiver entre aspas duplas ele é considerado uma String
#Dessa forma o sinal de + funciona como concatenar e não como uma soma.

#Integer
#Número interiro

print(123+345)
#Números, sejam iteiros ou não, não devem ser colocados entre aspas
#Ao preencher os número sem as aspas e com o sinal + obtemos a soma dos valores.

print(123_456_789)
#para facilitar a leitura de números grandes podemos colunas no lugar o separador de milhar o underlihe (_)
#Em PT o separadar é o . em EN é a ,

#Float
#Números decimais.

print(3.14159)

#O separador de decimais no PY é o .

#Boolean
#Verdadeiro / Falso

print(True)
print(False)

#Devem ser descritos com a primeira letra maiúsculas e sem aspas