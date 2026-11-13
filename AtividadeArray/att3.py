'''
3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 (121 dias) 
não ocorreu temperatura inferior a 15° C e nem superior a 40° C. Fazer um programa 
PY que determine: 
a) A menor temperatura ocorrida 
b) A maior temperatura ocorrida 
c) A temperatura média do período  
'''
somaTemps = 0
temps = [ ]

for i in range (4):
    temp = float(input(f"Digite qual foi a temperatura do {i+1}° mês: "))
    temps.append(temp)
    somaTemps += temp

print (f"A maior temperatura registrada foi: {max(temps)}")
print (f"A menor temperatura registrada foi: {min(temps)}")
print (f"A média das temperaturas registradas foi: {somaTemps/4}")