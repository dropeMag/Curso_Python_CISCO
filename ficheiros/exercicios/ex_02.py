arq_respostas = open("respostas.txt", mode="r+", encoding="utf-8")

tot_geral = tot_zumbi = tot_h = tot_h_hum40 = tot_m = tot_m_zum40_veg = 0

for linha in arq_respostas:
    linha = linha.split()
    tot_geral += 1

    if linha[0][0].upper() == "M":
        tot_h += 1
    else:
        tot_m += 1

    if linha[2][0].upper() == "S":
        tot_zumbi += 1
        if linha[0][0].upper() == "F" and linha[3][0].upper() == "S" and int(linha[1][:2]) >= 40:
            tot_m_zum40_veg += 1

    if linha[2][0].upper() == "N" and linha[0][0].upper() == "M" and int(linha[1][:2]) < 40:
        tot_h_hum40 += 1

print(f"Percentual de Zumbis: {tot_zumbi * 100 / tot_geral:.2f}%")
print(f"Percentual de Homens não Zumbis abaixo dos 40: {tot_h_hum40 * 100 / tot_h:.2f}%")
print(f"Percentual de Mulheres Zumbis Vegetarianas acima dos 40: {tot_m_zum40_veg * 100 / tot_m:.2f}%")

arq_respostas.close()
