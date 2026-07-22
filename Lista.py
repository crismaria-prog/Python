nome = "Joaquim Alameda"
email = "joaquimalameda@gmail.com"

#descubra o servidor do e-mail
posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

#pegar o primeiro nome do usuario
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)
#construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o e-mail tal
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o e-mail:{email}"
print (mensagem)
#contrua uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com
primeira_letra= email[0]

mensagem2 = f"Enviamos um link de confirmação para o email:{primeira_letra}***{servidor}"
print(mensagem2)