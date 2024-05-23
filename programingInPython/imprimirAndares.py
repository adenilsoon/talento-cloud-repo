# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
#cComo desafio, imprima eles em ordem decrescente (20, 19, 18...)


# Imprimir andares em ordem descrescente, exceto o 13°, utilizando o FOR
for i in range(21, 0, -1):
   if (i != 13):
        print("Bem-Vindo ao " + str(i) + "° andar!")

print("\n")

# Imprimir andares em ordem descrescente, exceto o 13°, utilizando o WHILE
numeroAndar = 21
while(numeroAndar >= 1):
    if(numeroAndar != 13):
        print("Bem-Vindo ao " + str(numeroAndar) + "° andar!")
    numeroAndar-=1