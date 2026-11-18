'''
3- Faça um programa que leia e monte dois vetores de números inteiros 
com 20 números cada. Depois de montados, gere um terceiro vetor formado pela diferença 
dos dois vetores lidos, um quarto vetor formado pela soma dos dois vetores lidos e por 
último um quinto vetor formado pela multiplicação dos dois vetores lidos.
'''
vetor1 = [ ]
vetor2 = [ ]
vetor3 = [ ]
vetor4 = [ ]
vetor5 = [ ]

for i in range (5):
    n1 = int(input("Digite um número: "))
    vetor1.append(n1)
    n2 = int(input("Digite um número: "))
    vetor2.append(n2)

vetor3.append(vetor1[i]-vetor2[i])
vetor4.append(vetor1[i]+vetor2[i])
vetor5.append(vetor1[i]*vetor2[i])

print (vetor1)
print (vetor2)
print (vetor3)
print (vetor4)
print (vetor5)