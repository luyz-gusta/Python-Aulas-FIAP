import random

correct_play = 0
total_gamed = 0


exec_again = True
list = [1, 2, 3]
listOptions = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura"
}

def check_gamed( option_bot: int,  option_user: int):
    retorno = ""

    if  option_user == 3 and  option_bot == 1:
        retorno = f"Bot Venceu! \nBot: {listOptions[ option_bot]} \nUser: {listOptions[ option_user]}"
    elif  option_bot == 3 and  option_user == 1:
        retorno = f"User Venceu! \nBot: {listOptions[ option_bot]} \nUser: {listOptions[ option_user]}"
    elif  option_bot >  option_user:
        retorno = f"Bot Venceu! \nBot: {listOptions[ option_bot]} \nUser: {listOptions[ option_user]}"
    elif  option_bot <  option_user:
        retorno = f"User Venceu! \nBot: {listOptions[ option_bot]} \nUser: {listOptions[ option_user]}"
    else:
        retorno = f"Empate !! \nBot: {listOptions[ option_bot]} \nUser: {listOptions[ option_user]}"
    return retorno

print("*************** Jokenpo ***************")
while exec_again == True:
    print("Escolha a sua jogada: ")
    print("(1) - Pedra")
    print("(2) - Papel")
    print("(3) - Tesoura")
    option_user = int(input())
    option_bot = random.choice(list)

    try:
        print(check_gamed( option_bot,  option_user))
    except:
        print("Opção inválida! Jogue novamente")
    finally:
        again = input("Deseja jogar novamente?(Y/N)\n")
        if again.lower() == "y":
            exec_again = True
        else:
            exec_again = False
            print("Obrigado por jogar !!")

