
Vendas = input("Digite suas vendas do dia: ")
Vendas = float(Vendas)

# Tambem posso fazer com o float junto com input
# Vendas = float(input("Digite suas vendas do dia: "))

bonus = Vendas * 0.01
print(bonus)

# cuidado de esquecer de incluir o float qndo for fazer conta, é necessario 1 float para cada variavel
# Exemplo

Vendas_dia1 = input("Vendas dia 1: ")
Vendas_dia2 = input("Vendas dia 2: ")
print(f"Total de vendas:{float(Vendas_dia1)+float(Vendas_dia2)}")