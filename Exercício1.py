nome = "Cris Marques"
email = "crismarques@gmail.com"

# descubra o servidor
posicao = email.find("@")
print(posicao) # somente para teste
servidor = email[posicao:]
print(servidor)

#pegar o 1º nome do usuario
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# construa uma mensagememail: Usuario primeiro_nome cadastrado com sucesso com o e-mail tal
mensagem = f"Usuário {primeiro_nome}, cadastrado com sucesso com o email: {email}"
print(mensagem)

# construa uma mensagem: Enviamos um link de confirmação para o e-mail j***@gmail.com
primeiro_letra = email[0]
print(primeiro_letra)
mensagem2 = f"Enviamos um link de confirmação para o email{primeiro_letra}***{servidor}"
