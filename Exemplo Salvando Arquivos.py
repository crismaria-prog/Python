# EXEMPLOS DE COMO SALVAR ARQUIVOS EM PYTHON
# O arquivo será criado na mesma pasta do programa.

# Nome do arquivo que será criado
nome_arquivo = "cadastro.txt"

# ---------------------------------------------------
# 1. CRIANDO E SALVANDO INFORMAÇÕES EM UM ARQUIVO | Adicionando mais conteúdo sem apagar o que já existe (modo "a")
# ---------------------------------------------------

# O modo "w" significa write, ou seja, escrever.
# Caso o arquivo não exista, ele será criado.
# Caso já exista, o conteúdo anterior será apagado.

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome: Carlos\n")
    arquivo.write("Idade: 25 anos\n")
    arquivo.write("Cidade: Florianópolis\n")

print("Arquivo criado e informações salvas com sucesso!")


# ---------------------------------------------------
# 2. LENDO O CONTEÚDO DO ARQUIVO | Lendo todo o conteúdo do arquivo (modo "r")
# ---------------------------------------------------

# O modo "r" significa read, ou seja, leitura.

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("\nConteúdo do arquivo:")
print(conteudo)


# ---------------------------------------------------
# 3. ADICIONANDO NOVAS INFORMAÇÕES
# ---------------------------------------------------

# O modo "a" significa append, ou seja, adicionar.
# Ele mantém o conteúdo anterior e adiciona novas informações.

with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write("Profissão: Desenvolvedor\n")
    arquivo.write("Empresa: Empresa Exemplo\n")

print("Novas informações adicionadas com sucesso!")


# ---------------------------------------------------
# 4. LENDO NOVAMENTE O ARQUIVO ATUALIZADO |  Lendo o arquivo linha por linha
# ---------------------------------------------------

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo_atualizado = arquivo.read()

print("\nConteúdo atualizado:")
print(conteudo_atualizado)


# ---------------------------------------------------
# 5. SALVANDO INFORMAÇÕES DIGITADAS PELO USUÁRIO
# ---------------------------------------------------

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
cidade = input("Digite a sua cidade: ")

with open("dados_usuario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("DADOS DO USUÁRIO\n")
    arquivo.write("--------------------\n")
    arquivo.write("Nome: " + nome + "\n")
    arquivo.write("Idade: " + idade + "\n")
    arquivo.write("Cidade: " + cidade + "\n")

print("\nDados do usuário salvos no arquivo dados_usuario.txt!")


# ---------------------------------------------------
# 6. SALVANDO VÁRIOS NOMES EM UM ARQUIVO
# ---------------------------------------------------

nomes = []

for contador in range(3):
    nome_digitado = input("Digite um nome: ")
    nomes.append(nome_digitado)

with open("lista_nomes.txt", "w", encoding="utf-8") as arquivo:
    for nome_salvo in nomes:
        arquivo.write(nome_salvo + "\n")

print("\nLista de nomes salva no arquivo lista_nomes.txt!")


# ---------------------------------------------------
# 7. MOSTRANDO OS NOMES SALVOS
# ---------------------------------------------------

with open("lista_nomes.txt", "r", encoding="utf-8") as arquivo:
    print("\nNomes salvos no arquivo:")

    for linha in arquivo:
        print(linha.strip())