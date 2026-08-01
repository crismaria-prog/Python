# EXEMPLOS DE ARRAY EM PYTHON
# Em Python, usamos listas para armazenar vários valores
# dentro de uma única variável.

# Criando um array de números
numeros = [10, 20, 30, 40, 50]

# Exibindo o array completo
print("Array completo:")
print(numeros)

# Cada elemento possui uma posição chamada índice.
# Os índices começam em 0.
#
# Índices:  0   1   2   3   4
# Valores: 10  20  30  40  50

# Exibindo elementos específicos
print("\nPrimeiro elemento:")
print(numeros[0])

print("\nTerceiro elemento:")
print(numeros[2])

# Alterando um elemento
numeros[1] = 25

print("\nArray após alterar o segundo elemento:")
print(numeros)

# Adicionando um novo elemento no final
numeros.append(60)

print("\nArray após adicionar o número 60:")
print(numeros)

# Removendo um elemento pelo valor
numeros.remove(30)

print("\nArray após remover o número 30:")
print(numeros)

# Mostrando a quantidade de elementos
print("\nQuantidade de elementos:")
print(len(numeros))

# Percorrendo todos os elementos com for
print("\nElementos do array:")

for numero in numeros:
    print(numero)

# Verificando se um valor está no array
numero_pesquisado = 40

if numero_pesquisado in numeros:
    print("\nO número", numero_pesquisado, "está no array.")
else:
    print("\nO número", numero_pesquisado, "não está no array.")

# Criando um array com valores digitados pelo usuário
nomes = []

print("\nCadastro de nomes:")

for contador in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("\nNomes cadastrados:")

for nome in nomes:
    print(nome)