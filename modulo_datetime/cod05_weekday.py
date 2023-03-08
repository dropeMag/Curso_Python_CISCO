from datetime import date

hoje = date.today()
dia = hoje.weekday()

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

print(f"Hoje é {dias[dia]}")
