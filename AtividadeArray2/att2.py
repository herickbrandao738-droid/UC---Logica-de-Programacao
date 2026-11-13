'''
2- Utilizando vetores, crie um programa que organize uma quantidade qualquer de 
números inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em 
ordem crescente e depois os números ímpares em ordem decrescente. 
'''


np = [ ]
ni = [ ]

while True:
    n = int(input("Digite um número: "))

    if n % 2 == 0:
        np.append(n)
    else:
        ni.append(n)

    print (f"O números pares são: {np}")
    print (f"O números ímpares são: {ni}")
    np.sort()
    ni.sort(reverse=True)
    print (f"A ordem dos números pares fica: {np}")
    print (f"A ordem dos números ímpares fica: {ni}")