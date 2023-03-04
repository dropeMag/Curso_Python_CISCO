import random

try:
    num_pessoas = int(input("Informe quantos nome deseja adicionar: "))
    num_nomes = 0

    arq_nomes = open("nomes.txt", mode="rt", encoding="utf-8")

    for linha in arq_nomes:
        num_nomes += 1

    arq_nomes.close()


    arq_pessoas = open("saida.txt", mode="a+", encoding="utf-8")

    for pes in range(num_pessoas):
        arq_nomes = open("nomes.txt", mode="rt", encoding="utf-8")
        arq_sobrenomes = open("sobrenomes.txt", mode="rt", encoding="utf-8")

        val_nome = random.randint(1, num_nomes)
        val_sobr = random.randint(1, num_nomes)

        pes_nome = pes_sobr = ''

        for x in range(val_nome):
            pes_nome = arq_nomes.readline()

        for x in range(val_sobr):
            pes_sobr = arq_sobrenomes.readline()

        pes_idad = random.randint(1, 100)

        arq_pessoas.write(f"{pes_nome.strip()} {pes_sobr.strip()} {pes_idad}\n")

        arq_nomes.close()
        arq_sobrenomes.close()

    arq_pessoas.close()
except BaseException as err:
    print("Não foi possível realizar a ação.")
    print("Erro:", err)
else:
    print("Ação realizada com sucesso!")
