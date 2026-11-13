'''
1- Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. 
No final, mostre:
a) Qual é a média da turma-
b) Quantos alunos estão acima da média da turma -
c) Qual foi a maior nota digitada-
d) Em que posições a maior nota aparece- 
'''
notasAcimaMedia = 0
notas = [ ]
mediaNotas = 0
notaTotal = 0
maiorNota = 0

for i in range (10):
    nota = float (input(f"Digite a nota do {i+1}° aluno: "))
    notas.append(nota)
    notaTotal += nota
    mediaNotas = notaTotal/10
for i in range (len(notas)):
    if notas[i] > mediaNotas:
        notasAcimaMedia += 1

print (f"A média da turma é: {mediaNotas}")
print (f"A maior nota da turma é: {max(notas)}")
print (f"{notasAcimaMedia} notas estão acima da média.")

for i in range (len(notas)):
    if notas[i] > maiorNota:
        maiorNota = notas[i]
        posicao = i

        print ("A maior nota está na posição: ", posicao )
