
#FORMATAÇÃO NUMERICAS ESPECIAIS
# Na frente da variavel coloca 2 pontos (:), 1 ponto (.) que é para indicar que vai ter uma casa decimal
# 2 é para dizer quantas casa decimais você quer e f é para indicar que é do tipo floar
# a vircula (,) para separar a milar
# Exemplo:

print (f "FATURAMENTO: R${FATURAMENTO:,.2F }, CUSTO: {CUSTO}, LUCRO: {LUCRO}")

# Outro exemplo é para caso queira utilizar porcentagem
# .1% - o 1 ira indicar quantas casas decimais vc quer que apareça, caso não queira que apareça nenhuma
# é só colocar .0%
# Exemplo:

print(f"MARGEM: {MARGEM:.1%}")

# Para fazer a separação dentro de uma string utilizamos o contrabarra n ( \n ), lembrando que para separação
# só pode utilizar dentro de uma str 
# Exemplo:

print (f "FATURAMENTO: R${FATURAMENTO:,.2F}\n, CUSTO: {CUSTO}\n, LUCRO: {LUCRO}\n")
