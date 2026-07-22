km = float(input("Digite a distância em quilômetros: "))

print("Converter para:")
print("1 - Metros")
print("2 - Centímetros")
print("3 - Milímetros")
print("4 - Milhas")
print("5 - Jardas")
print("6 - Polegadas")

opcao = input("Escolha a opção (1-6): ").strip()

if opcao == "1":
    resultado = km * 1000
    unidade = "metros"
elif opcao == "2":
    resultado = km * 100000
    unidade = "centímetros"
elif opcao == "3":
    resultado = km * 1000000
    unidade = "milímetros"
elif opcao == "4":
    resultado = km * 0.621371
    unidade = "milhas"
elif opcao == "5":
    resultado = km * 1093.6133
    unidade = "jardas"
elif opcao == "6":
    resultado = km * 39370.0787
    unidade = "polegadas"
else:
    print("Opção inválida.")
    resultado = None

if resultado is not None:
    print(f"{km:.3f} km = {resultado:.3f} {unidade}")