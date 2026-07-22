ID_da_Venda = int(input("Digite o ID da Venda: "))
Data = input("Digite a data da venda: ")
Vendedor = input("Digite o nome do vendedor: ")
Cliente = input("Digite o nome do cliente: ")
Produto = input("Digite o nome do produto: ")
Categoria = input("Digite a Categoria: ")
Quantidade = int(input("Digite a quantidade: "))
Preco_unitario = float(input("Digite o preço unitário: R$ "))



# Valor total com desconto ou a prazo

# exercicio : Se QTD > 100 --> Informar que não possui estoque
if Quantidade > 100:
    print("Sem estoque")
else:
    valor_total = Quantidade * Preco_unitario
    # Se for avista tem desconto 5%, a prazo +5%
    forma_pagamento = input("Forma de pagamento: ").strip().lower()
    if forma_pagamento in ("avista", "a vista"):
        valor_final = valor_total * 0.95
    elif forma_pagamento in ("aprazo", "a prazo", "prazo"):
        valor_final = valor_total * 1.05
    else:
        print("Forma de pagamento inválido. Será considerado à vista!")
        valor_final = valor_total * 0.95



print("\n" + "=" * 40)
print("   DADOS DA VENDA   ")
print("=" * 40)
print(f"ID da venda: {ID_da_Venda}")
print(f"Data: {Data}")
print(f"Vendedor: {Vendedor}")
print(f"Cliente: {Cliente}")
print(f"Produto: {Produto}")
print(f"Categoria: {Categoria}")
print(f"Quantidade: {Quantidade}")
print(f"Preço Unitário: {Preco_unitario}")
print(f"Valor Total: R$ {valor_total:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
print("=" * 40)