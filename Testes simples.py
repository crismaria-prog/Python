# Exercícios 
nome = input("Digite o seu nome: ").strip().title()
email = input("Digite o seu email: ").strip().lower()

# Descubra o servidor do email

# essa é uma forma bem simples de fazer porém pode dar erro, a melhor é utilizado if, elif e else. Como destacarei abaixo
#posicao = email.find("@")  
#servidor = email[posicao:]
#print(servidor)


if not nome:
   print("O campo nome não pode ficar vazio!\n Tente novamente!")

elif '@' not in email:
   print ("E-mail inválido!\n O e-mail deve conter @.")

elif email:
   primeiro_nome = nome.split()[0]
   posicao = email.find("@")
   servidor = email[posicao:]


else:
   print("Tente novamente mais tarde!")


# Pegar o primeiro nome do usuario
#posicao = nome.find(" ")
#usuario = nome[:posicao]
#print(usuario)

# Construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com 

mensagem = (f"\nUsuario {primeiro_nome}, cadastrado com sucesso com o email {email} ")
print(mensagem)

# email tal (sempre que alterar a variavel o código do email deve funcionar tranquilo)

# Contrua uma mensagem:  Enviamos um link de confirmação para o email j***@gmail.com

primeira_letra = email[0]

mensagem2 = (f"\nEnviamos um link de confirmação para o email {primeira_letra}***{servidor}")
print (mensagem2)
print()

