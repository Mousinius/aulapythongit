""""
comandos condicionais, são comandos que efetuam desvios no fluxo do programa

comando if - se alguma coisa for verdadeira, faça isto, caso contrário, faça aquilo

SINTAXE:
print(conteúdo)
conteúdo de texto entre aspas duplas, conteúdo de número sem aspas

if teste-condicional
    faça algo
else:
    faça a negação

"""
idade = 15
if idade >=18:
    print("maior de idade")
else:
    print("vá pra disney")

"""
um parque de diversões que cobra preços diferentes para grupos etários
entre 4 e 18 custa R$ 5 reais
acima de 18 custa R$ 20 reais

"""

age = 12

if age < 4:
    print("de graça")
elif age < 18:
    print("5")
else:
    print("20")

print("--------------")

if age <= 4:
    preco = 0
elif age<=18:
    preco = 5
else:
    preco = 20
print("sua entrada custara", preco)

# entrada de dados utilizando o input

mensagem = input("digite o seu nome:")
print("olá "+mensagem+" bem vindo")
idade = input("digite a sua idade: ")
idade = int(idade)
print(idade, type(idade))
