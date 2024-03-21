exec_again = True

while exec_again == True:
    # Exercicio 1
    cont = 0
    print("------------- Pares -------------")
    while cont <= 20:
        if cont % 2 == 0:
            print(f"{cont}")
        cont += 1

    # Exercicio 2
    print("------------- Tabuada do 7 -------------")
    index = 1
    while (index <= 10):
        print(f"7 x {index} = {7 * index}")
        index += 1

    # Exercicio 3
    print("----------------------------------------")
    again = input("Deseja executar novamente?(Y/N)\n")
    if again.lower() == "y":
        exec_again = True
    else:
        exec_again = False