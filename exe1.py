"""
crie um algoritmo que receba 3 notas. calcule a média aritmetica
se a média for maior que 7, exibir mensagem de aprovado, caso contrário, reprovado

"""
n1 = 7
n2 = 7
n3 = 7
media = (n1+n2+n3)/3

print(media)
if media <= 4.09:
    print("reprovado")
elif media < 6:
    print("recuperação")
else:
    print("boa")