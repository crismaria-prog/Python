# EXEMPLOS DE VETOR EM PYTHON
# Em Python, normalmente usamos uma lista para representar um vetor.


# ---------------------------------------------------
# 1. CRIANDO UM VETOR
# ---------------------------------------------------

numeros = [10, 20, 30, 40, 50]

print("Vetor completo:")
print(numeros)


# ---------------------------------------------------
# 2. ACESSANDO POSIÇÕES DO VETOR
# ---------------------------------------------------

# As posições começam em 0.
#
# Posição:  0   1   2   3   4
# Valor:   10  20  30  40  50

print("\nPrimeiro valor:")
print(numeros[0])

print("\nTerceiro valor:")
print(numeros[2])

print("\nÚltimo valor:")
print(numeros[-1])


# ---------------------------------------------------
# 3. ALTERANDO UM VALOR
# ---------------------------------------------------

numeros[1] = 25

print("\nVetor após alterar o segundo valor:")
print(numeros)


# ---------------------------------------------------
# 4. ADICIONANDO UM NOVO VALOR
# ---------------------------------------------------

numeros.append(60)

print("\nVetor após adicionar o número 60:")
print(numeros)


# ---------------------------------------------------
# 5. REMOVENDO UM VALOR
# ---------------------------------------------------

numeros.remove(30)

print("\nVetor após remover o número 30:")
print(numeros)


# ---------------------------------------------------
# 6. MOSTRANDO A QUANTIDADE DE ELEMENTOS
# ---------------------------------------------------

quantidade = len(numeros)

print("\nQuantidade de elementos no vetor:")
print(quantidade)


# ---------------------------------------------------
# 7. PERCORRENDO O VETOR COM FOR
# ---------------------------------------------------

print("\nValores do vetor:")

for numero in numeros:
    print(numero)


# ---------------------------------------------------
# 8. PERCORRENDO O VETOR COM POSIÇÕES
# ---------------------------------------------------

print("\nPosições e valores:")

for posicao in range(len(numeros)):
    print("Posição:", posicao, "- Valor:", numeros[posicao])


# ---------------------------------------------------
# 9. VERIFICANDO SE UM VALOR EXISTE
# ---------------------------------------------------

numero_pesquisado = 40

if numero_pesquisado in numeros:
    print("\nO número", numero_pesquisado, "está no vetor.")
else:
    print("\nO número", numero_pesquisado, "não está no vetor.")


# ---------------------------------------------------
# 10. SOMANDO OS VALORES
# ---------------------------------------------------

soma = sum(numeros)

print("\nSoma dos valores:")
print(soma)


# ---------------------------------------------------
# 11. ENCONTRANDO O MAIOR E O MENOR VALOR
# ---------------------------------------------------

maior_numero = max(numeros)
menor_numero = min(numeros)

print("\nMaior número:")
print(maior_numero)

print("\nMenor número:")
print(menor_numero)


# ---------------------------------------------------
# 12. CALCULANDO A MÉDIA
# ---------------------------------------------------

media = sum(numeros) / len(numeros)

print("\nMédia dos valores:")
print(media)


# ---------------------------------------------------
# 13. ORDENANDO O VETOR
# ---------------------------------------------------

numeros.sort()

print("\nVetor em ordem crescente:")
print(numeros)

numeros.sort(reverse=True)

print("\nVetor em ordem decrescente:")
print(numeros)


# ---------------------------------------------------
# 14. CRIANDO UM VETOR COM DADOS DO USUÁRIO
# ---------------------------------------------------

nomes = []

print("\nCadastro de nomes:")

for contador in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("\nVetor de nomes:")
print(nomes)


# ---------------------------------------------------
# 15. MOSTRANDO OS NOMES CADASTRADOS
# ---------------------------------------------------

print("\nNomes cadastrados:")

for nome in nomes:
    print(nome)


# ---------------------------------------------------
# 16. CRIANDO UM VETOR DE NOTAS
# ---------------------------------------------------

notas = []

for contador in range(3):
    nota = float(input("\nDigite uma nota: "))
    notas.append(nota)

media_notas = sum(notas) / len(notas)

print("\nNotas cadastradas:")
print(notas)

print("Média das notas:")
print(media_notas)