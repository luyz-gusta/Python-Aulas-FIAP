def formatacao():
    aluno = {
        'nome': 'Luiz',
        'n1': 6.3,
        'n2': 5.9,
        'n3': 9.8,
        'n4': 7.5
    }

    mf = (aluno['n1'] + aluno['n2'] + aluno['n3'] + aluno['n4']) / 4.0

    print("Nome             Nota 1               Nota 2               Nota 3               Nota 4               Média")
    print(f"{aluno['nome']:<17}{aluno['n1']:<21}{aluno['n2']:<21}{aluno['n3']:<21}{aluno['n4']:<21}{mf}")


def cal_media():
    print("************* Calculadora de média *************")

    exec = True
    while exec:
        nome = input("Digite o seu nome:")
        nota1 = float(input("Digite a nota 1:"))
        nota2 = float(input("Digite a nota 2:"))
        nota3 = float(input("Digite a nota 3:"))
        media = (nota1 + nota2 + nota3) / 3
        print("Nome             Nota 1               Nota 2               Nota 3               Média")
        print(f"{nome:<17}{nota1:<21.1f}{nota2:<21.1f}{nota3:<21.1f}{media:>2.1f}")

        option = input("Deseja executar novamente [S/N]? ").upper()
        if(option != "S"):
            exec = False

cal_media()