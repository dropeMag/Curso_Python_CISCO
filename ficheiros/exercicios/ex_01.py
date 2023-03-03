lst_classe = open("classe.txt", mode="rt", encoding="utf8")
lst_notas = open("notas.txt", mode="rt", encoding="utf8")

resp_user = input("Digite o nome ou número do aluno: ")

id_aluno = -1
nome_aluno = "inexistente!"

for linha in lst_classe:
    linha = linha.split()
    if resp_user in linha:
        id_aluno = linha[0]
        nome_aluno = linha[1]

if id_aluno == -1:
    print("Aluno", nome_aluno)
else:
    for linha in lst_notas:
        linha = linha.split()
        if id_aluno == linha[0]:
            print("Aluno:", nome_aluno)
            print("Notas:", end=' ')
            for nota in linha[1:]:
                print(nota, end=" ")

lst_classe.close()
lst_notas.close()
