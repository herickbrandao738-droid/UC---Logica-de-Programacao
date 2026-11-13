'''
1- Faça um programa em Py que receba o total das vendas de 
cada vendedor e armazenadas em um vetor. Receba também o percentual 
de comissão de cada vendedor e armazene-os em outro vetor. Receba os 
nomes desses vendedores e armazene ­os em um terceiro vetor. Existem apenas 
dez vendedores. Calcule e mostre: 
a) Um relatório com os nomes dos vendedores e os valores a receber; 
b) O total das vendas de todos os vendedores; 
c) O maior valor a receber e quem o receberá; 
d) O menor valor a receber e quem o receberá.
'''
vendasTotal = 0
nomeVendedor = [ ]
percentualVendedor =  [ ]
totalVendas = [ ]

for i in range (2):
    nome = str(input(f"Digite o nome do {i+1}° vendedor: "))
    nomeVendedor.append(nome)

    percentual = float(input("Digite o percentual de comissão: "))
    percentualVendedor.append(percentual)

    vendas = float(input("Digite o total de vendas: "))
    totalVendas.append(vendas)
    vendasTotal += vendas

for i in range (2):
    print (f"O vendedor {nomeVendedor[i]} receberá um total de {totalVendas[i]*(percentualVendedor[i]/100)}")

maiorVenda = max(totalVendas)
posicao1 = totalVendas.index(maiorVenda)

menorVenda = min(totalVendas)
posicao2 = totalVendas.index(menorVenda)
print (f"O total de vendas de todos os vendedores foi {vendasTotal}")
print (f"O maior valor da lista foi de: {maiorVenda} \nE o vendedor foi o {nomeVendedor[posicao1]}")
print (f"O menor valor da lista foi de: {menorVenda} \nE o vendedor foi o {nomeVendedor[posicao2]}")