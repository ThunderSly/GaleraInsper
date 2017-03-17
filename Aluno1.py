def Numeros():
	lista=[]
	x=int(input("Digite quantos numero quer adicionar a lista: "))
	for i in range(x):
		y=int(input("Digite o numero que deseja adicionar a lista: "))
		lista.append(y)
	return lista
lista=Numeros()


