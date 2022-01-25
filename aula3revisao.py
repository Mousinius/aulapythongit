nome = 'JUAN'
idade = 19
peso = 98.78
altura = 1.88
curso = 'ADS'
print(idade, type(idade))
print("me chamo "+nome+", tenho", idade, "anos, estudei o curso de "+curso)

if idade > 18:
    print("maior de idade")
elif idade < 10:
    print("você precisa ter mais de 10")
else:
    print("menor de idade")