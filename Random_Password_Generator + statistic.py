import string
import random
senhaALEATORIA = ''
mincarac = 6
maxcarac = 23
#Mude os valores acima para ver como os resultados se comportam
totalcarac = random.randint(mincarac, maxcarac) #Quantas caracteres a senha vai ter (Priemiro valor = min caracteres. Segundo valor = max caracteres)
tot20 = tot15 = tot10 = totless10 = 0
vezes = 1000 #escolha do tanto de vezes que o codigo vai rodar
count = 0
 

while vezes != count:  #Quantas vezes o codigo vai rodar
    while len(senhaALEATORIA) != totalcarac: #Enquanto a senha não tiver o tanto de caracteres
        a = random.choice(string.ascii_letters + string.digits)
        senhaALEATORIA += a
        if len(senhaALEATORIA) == totalcarac: #Contador do tamanho da senha
            if len(senhaALEATORIA) >= 20:
                tot20+=1
            elif len(senhaALEATORIA) >= 15:
                tot15+=1
            elif len(senhaALEATORIA) >= 10:
                tot10+=1
            elif len(senhaALEATORIA) < 10:
                totless10+=1
    count+=1
    senhaALEATORIA = ''
    totalcarac = random.randint(6, 23)
print('#' * 50)   
print(f'Tivemos um total de {tot20} senhas com 20 caracteres')
print(f'Tivemos um total de {tot15} senhas entre 15 e 19 caracteres')
print(f'Tivemos um total de {tot10} senhas entre 10 e 14 caracteres')
print(f'Tivemos um total de {totless10} senhas com menos de 10 caracteres')
 