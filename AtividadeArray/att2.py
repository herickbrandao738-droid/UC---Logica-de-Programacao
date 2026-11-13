'''
2- Faça um programa em Py que leia um vetor de seis elementos numéricos inteiros, 
calcule e mostre: 
a) A quantidade de números pares 
b) Quais os números pares 
c) A quantidade de números ímpares 
d) Quais os números ímpares
'''
par = [ ]
impar = [ ]
for i in range (6):
    n = int(input("Digite um número inteiro: "))

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print (f"A quantidade de números pares foi: {len(par)}")
print (f"O números pares foram: {par}")
print (f"A quantidade de números ímpares foi: {len(impar)}")
print (f"Os números ímpares foi: {impar}")