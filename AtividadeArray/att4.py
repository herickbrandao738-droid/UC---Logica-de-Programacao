'''
4- Faça um programa em Py que alimente um vetor, com um número de posições 
definidas pelo usuário. Este vetor deverá armazenar um conjunto de nomes em 
diferentes posições. Crie um mecanismo para alimentar elementos no vetor e pesquisar 
por um valor existente.
 ======== MENU ======== 
1) Cadastrar nome 
2) Pesquisar nome 
3) Listar todos os nome 
0) Sair do programa 
——————– 
Digite sua escolha:
'''

nome = [ ]
while True:
    print ("======== MENU ========")
    print ("1) Cadastrar nome ")
    print ("2) Pesquisar nome ")
    print ("3) Listar todos os nomes ")
    print ("0) Sair do programa ")
    print ("——————– ")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 0:
        break
    elif escolha == 3:
        print (nome)
    elif escolha == 2:
        posi = str(input("Qual nome você gostaria de encontrar?: "))
        if posi in nome: 
            print ("O nome que você está procurando esá na posição: ", nome.index(posi))
        else:
            print ("Nome não encontrado.")
    elif escolha == 1:
        conj = int(input("Digite quantos nomes você irá adicionar: "))
        for i in range (conj):
            novoNome = str(input("Digite um nome: "))
            nome.append (novoNome)
    else:
        print ("Número inválido")
        continue