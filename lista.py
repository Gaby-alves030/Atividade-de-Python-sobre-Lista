lista = []

while True:
    usuario = int(input("Digite um valor: "))
    if usuario < 0:
        break
    lista.append(usuario)
print(lista)
