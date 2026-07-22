
senha = input("Digite a senha: ")

while senha != "1234":
    print("Senha incorreta. Tente novamente;")
    senha= input("Digite a senha:")
print("Acesso concedido. Bem-vindo!")

contador = 1
soma = 0
while contador <= 5:
    numero = int(input(f"Digite o {contador}º número: "))
    soma =  10 + 5 * numero
    contador = contador +1
