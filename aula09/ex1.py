
# cont = 1
# while cont <= 10:
#     print(cont)
#     cont+=1

print("************** Exercicio 1 **************")

linhas = int(input("Quantas linhas? "))
#colunas = int(input("Quantas colunas? "))
# for cont in range(0,linhas,1):
#     print("#" * colunas)

# for cont in range(0,linhas,1):
#     if(cont == 0 or cont == linhas -1):
#         print("#" * colunas)
#     else:
#         print(f"{'#':<{colunas - 1}}#")

# for cont in range(0, linhas, 1):
#     for num in range(1, colunas + 1, 1):
#         print(num, end="")
#     print("")

spacer = linhas -1
for cont in range(1, linhas * 2, 2):
    print(" " * spacer, end="")
    print("*" * cont)
    spacer-=1
print((f"{' ':<{linhas - 2}}" + "| |\n") * 2)

# for cont in range(1, linhas * 2, 2):
#     print(f"{' ':<{linhas}}" + "*" * cont)
#     linhas -= 1

# n = 1
# for cont in range(0, linhas):
#     print(' ' * (linhas - 1), end="")
#     print("*" * (n))
#     linhas -= 1
#     n += 2