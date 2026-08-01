# EXEMPLOS DE MATRIZ EM PYTHON
# Uma matriz é formada por linhas e colunas.
# Em Python, usamos uma lista dentro de outra lista.


# ---------------------------------------------------
# 1. CRIANDO UMA MATRIZ
# ---------------------------------------------------

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Matriz completa:")
print(matriz)


# A matriz acima possui 3 linhas e 3 colunas:
#
#         Coluna 0   Coluna 1   Coluna 2
# Linha 0    10         20         30
# Linha 1    40         50         60
# Linha 2    70         80         90


# ---------------------------------------------------
# 2. ACESSANDO UM ELEMENTO DA MATRIZ | Acessando um elemento específico (linha 1, coluna 2)
# ---------------------------------------------------

# Primeiro informamos a linha e depois a coluna.

print("\nElemento da linha 0 e coluna 0:")
print(matriz[0][0])

print("\nElemento da linha 1 e coluna 2:")
print(matriz[1][2])

print("\nElemento da linha 2 e coluna 1:")
print(matriz[2][1])


# ---------------------------------------------------
# 3. MOSTRANDO UMA LINHA COMPLETA
# ---------------------------------------------------

print("\nPrimeira linha:")
print(matriz[0])

print("\nSegunda linha:")
print(matriz[1])


# ---------------------------------------------------
# 4. ALTERANDO UM ELEMENTO
# ---------------------------------------------------

matriz[1][1] = 55

print("\nMatriz após alterar o número 50 para 55:")
print(matriz)


# ---------------------------------------------------
# 5. MOSTRANDO A MATRIZ LINHA POR LINHA | Percorrendo e exibindo a matriz
# ---------------------------------------------------

print("\nMatriz organizada:")

for linha in matriz:
    print(linha)


# ---------------------------------------------------
# 6. MOSTRANDO CADA ELEMENTO SEPARADAMENTE
# ---------------------------------------------------

print("\nTodos os elementos:")

for linha in matriz:
    for numero in linha:
        print(numero)


# ---------------------------------------------------
# 7. MOSTRANDO LINHAS, COLUNAS E VALORES
# ---------------------------------------------------

print("\nPosições e valores da matriz:")

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(
            "Linha:",
            linha,
            "- Coluna:",
            coluna,
            "- Valor:",
            matriz[linha][coluna]
        )


# ---------------------------------------------------
# 8.1 SOMANDO TODOS OS ELEMENTOS 
# ---------------------------------------------------

soma = 0

for linha in matriz:
    for numero in linha:
        soma = soma + numero

print("\nSoma de todos os elementos:")
print(soma)

# ---------------------------------------------------
# 8.2 SOMANDO TODOS OS ELEMENTOS 
# ---------------------------------------------------
# Somando todos os elementos da matriz

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento


print("Soma de todos os elementos:", soma)


# ---------------------------------------------------
# 9. ENCONTRANDO O MAIOR E O MENOR VALOR
# ---------------------------------------------------

maior_numero = matriz[0][0]
menor_numero = matriz[0][0]

for linha in matriz:
    for numero in linha:

        if numero > maior_numero:
            maior_numero = numero

        if numero < menor_numero:
            menor_numero = numero

print("\nMaior número:")
print(maior_numero)

print("\nMenor número:")
print(menor_numero)


# ---------------------------------------------------
# 10.1 SOMANDO CADA LINHA
# ---------------------------------------------------

print("\nSoma de cada linha:")

for linha in matriz:
    soma_linha = sum(linha)
    print("Linha:", linha, "- Soma:", soma_linha)

# ---------------------------------------------------
# 10.2 SOMANDO CADA LINHA
# ---------------------------------------------------
    # Calculando a soma de cada linha
    
print("\nSoma de cada linha:")
for i, linha in enumerate(matriz):
    print(f"Linha {i}: {sum(linha)}")


# ---------------------------------------------------
# 11. MOSTRANDO A QUANTIDADE DE LINHAS E COLUNAS
# ---------------------------------------------------

quantidade_linhas = len(matriz)
quantidade_colunas = len(matriz[0])

print("\nQuantidade de linhas:")
print(quantidade_linhas)

print("\nQuantidade de colunas:")
print(quantidade_colunas)


# ---------------------------------------------------
# 12. CRIANDO UMA MATRIZ COM DADOS DO USUÁRIO
# ---------------------------------------------------

nova_matriz = []

print("\nDigite os valores da nova matriz:")

for linha in range(2):
    nova_linha = []

    for coluna in range(3):
        numero = int(
            input(
                "Digite o valor da linha "
                + str(linha)
                + " e coluna "
                + str(coluna)
                + ": "
            )
        )

        nova_linha.append(numero)

    nova_matriz.append(nova_linha)


# ---------------------------------------------------
# 13. MOSTRANDO A MATRIZ CRIADA PELO USUÁRIO
# ---------------------------------------------------

print("\nMatriz criada pelo usuário:")

for linha in nova_matriz:
    print(linha)


# ---------------------------------------------------
# 14. EXEMPLO DE MATRIZ COM NOMES
# ---------------------------------------------------

funcionarios = [
    ["Ana", "Matriz", "Administrativo"],
    ["Carlos", "Filial 1", "Financeiro"],
    ["Mariana", "Filial 2", "Tecnologia"]
]

print("\nFuncionários cadastrados:")

for funcionario in funcionarios:
    print("Nome:", funcionario[0])
    print("Empresa:", funcionario[1])
    print("Setor:", funcionario[2])
    print("------------------------------")