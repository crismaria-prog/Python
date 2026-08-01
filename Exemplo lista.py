# itens = ["maçã", "pão", "leite"]
# print(itens[0])   # mostra "maçã"
# itens.append("ovo")  # adiciona "ovo" no final
# itens[1] = "bolo"    # troca "pão" por "bolo"

#---------------------------------------
#1. Criando uma lista
#---------------------------------------

nomes = ["Ana", "Carlos", "Mariana", "João"]

print(nomes)

#---------------------------------------
#2. Mostrando um item da lista

#A contagem das posições começa em 0.

nomes = ["Ana", "Carlos", "Mariana", "João"]

print(nomes[0])  # Ana
print(nomes[1])  # Carlos
print(nomes[2])  # Mariana

#---------------------------------------
#3. Adicionando um item

nomes = ["Ana", "Carlos"]

novo_nome = input("Digite um nome: ")

nomes.append(novo_nome)

print(nomes)

#---------------------------------------
#4. Removendo um item

nomes = ["Ana", "Carlos", "Mariana"]

nomes.remove("Carlos")

print(nomes)

#---------------------------------------
#5. Alterando um item

nomes = ["Ana", "Carlos", "Mariana"]

nomes[1] = "Pedro"

print(nomes)

#Resultado:
['Ana', 'Pedro', 'Mariana']

#---------------------------------------
#6. Percorrendo uma lista com for

nomes = ["Ana", "Carlos", "Mariana", "João"]

for nome in nomes:
    print(nome)

#---------------------------------------
#7. Lista de números

notas = [8.5, 7.0, 9.5, 6.0]

for nota in notas:
    print(nota)

#---------------------------------------
#8. Calculando a média das notas
notas = [8.5, 7.0, 9.5, 6.0]

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade

print("Soma das notas:", soma)
print("Quantidade de notas:", quantidade)
print("Média:", media)

#---------------------------------------
#9. Verificando se um item existe

nomes = ["Ana", "Carlos", "Mariana"]

nome_pesquisado = input("Digite o nome que deseja procurar: ")

if nome_pesquisado in nomes:
    print("O nome está na lista.")
else:
    print("O nome não está na lista.")


#---------------------------------------
#10. Cadastro simples de funcionários
funcionarios = []

quantidade = int(input("Quantos funcionários deseja cadastrar? "))

for contador in range(quantidade):
    nome = input("Digite o nome do funcionário: ")
    funcionarios.append(nome)

print("\nFuncionários cadastrados:")

for funcionario in funcionarios:
    print(funcionario)

#---------------------------------------
#11. Lista com nome e empresa

funcionarios = []

while True:
    nome = input("Digite o nome do funcionário: ")
    empresa = input("Digite a empresa: ")

    funcionario = [nome, empresa]
    funcionarios.append(funcionario)

    continuar = input("Deseja cadastrar outro? Digite sim ou não: ").lower()

    if continuar == "não" or continuar == "nao":
        break

print("\nFuncionários cadastrados:")

for funcionario in funcionarios:
    print("Nome:", funcionario[0])
    print("Empresa:", funcionario[1])
    print("-" * 30)

#---------------------------------------
#12. Exemplo completo para praticar

nomes = []

while True:
    print("\n1 - Adicionar nome")
    print("2 - Mostrar nomes")
    print("3 - Remover nome")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        nomes.append(nome)
        print("Nome adicionado com sucesso.")

    elif opcao == "2":
        if len(nomes) == 0:
            print("Nenhum nome cadastrado.")
        else:
            print("\nNomes cadastrados:")

            for nome in nomes:
                print(nome)

    elif opcao == "3":
        nome = input("Digite o nome que deseja remover: ")

        if nome in nomes:
            nomes.remove(nome)
            print("Nome removido com sucesso.")
        else:
            print("Nome não encontrado.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")