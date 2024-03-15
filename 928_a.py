lista = []
contador_list= []
def Contador(letras):
    num_A = letras.count('A')#3
    num_B = letras.count('B')#2
    num_C = letras.count('C')#4
    num_D = letras.count('D')#1
    batata = max(num_A,num_B,num_C,num_D)
    contador = 0

    if batata == num_B:  
        if contador == 0:  
            lista.append('B')
            contador+=1

    if batata == num_C:
        if contador == 0:
            lista.append('C')
        contador+=1
    
    if  batata == num_D:
        if contador == 0:
            lista.append('D')
        contador+=1

    if batata == num_A:
        if contador == 0:
            lista.append('A')
        contador+=1
    contador_list.append(contador)



quantidade  = int(input())

for x in range(quantidade):
    letras  = input ()
    Contador(letras)
count = 0 
for y in lista:
    if contador>1:
        print('0')
    else:
        print(y)
        count+=1


