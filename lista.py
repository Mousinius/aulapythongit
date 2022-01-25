# declaração de uma lista (nas outras linguagens chama-se ARRAY)
nomes = ['juan','kauanny','jorge','diogo','rafael','eduardo']
idades = [46,18,38,30,43,38]
print(nomes)

# listar um unico elemento da lista
print(nomes[2].title())
print(nomes[0].title())

#concatenar valores de listas
mensagem = "o aluno da posição 3 é o "+nomes[3].title()+" e a sua idade é",idades[3]
print(mensagem)

motos = ['honda', 'yamaha','kwasaki']
motos[0] = 'ducati'
print(motos)

#acrescentar valores a lista
motos[3] = 'honda'
print(motos)
