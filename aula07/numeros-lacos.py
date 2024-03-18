
#Exercicio 1
cont = 0
print("------------- Pares -------------")
while cont <= 20 :
    if cont % 2 == 0:
        print(f"{cont}")
    cont+=2

#Exercicio 2
print("------------- Tabuadas -------------")
multiplicador = 1
multiplicando = 1

while multiplicador <= 10:
    print(f"Tabuada do {multiplicador}: ")

    while multiplicando <= 10:
        print(f"{multiplicador} x {multiplicando} = {multiplicador * multiplicando}")
        multiplicando+=1

    multiplicando = 1
    multiplicador+=1
    print("-----------------------------")

# index = 1
# while(index <= 10):
#     print(f"7 x {index} = {7 * index}")
#     index+=1

