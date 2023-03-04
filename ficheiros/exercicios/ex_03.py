votos = open("votos.txt", mode="rt")

vt_bart = vt_homer = vt_krusty = vt_mrburns = vt_ned = vt_nulo = vt_total = 0
cnd_venc = cnd_perd = ""

for voto in votos:
    voto = int(voto)
    if voto == 1:
        vt_bart += 1
    elif voto == 2:
        vt_homer += 1
    elif voto == 3:
        vt_krusty += 1
    elif voto == 4:
        vt_mrburns += 1
    elif voto == 5:
        vt_ned += 1
    else:
        vt_nulo += 1

lst_candidatos = {"1 - Bart": vt_bart, "2 - Homer": vt_homer, "3 - Krusty": vt_krusty, "4 - Mr. Burns": vt_mrburns, "5 - Ned Flanders": vt_ned}

for candidato in lst_candidatos.items():
    if candidato[1] == max(lst_candidatos.values()):
        cnd_venc = candidato

    if candidato[1] == min(lst_candidatos.values()):
        cnd_perd = candidato

    vt_total += candidato[1]

print(f"CANDIDATO VENCEDOR: Candidato {cnd_venc[0]}, com {cnd_venc[1]} votos")
print(f"CANDIDATO PERDEDOR: Candidato {cnd_perd[0]}, com {cnd_perd[1]} votos")
print(f"TOTAL VOTOS: {vt_total}")
print(f"TOTAL NULOS: {vt_nulo}")

votos.close()
