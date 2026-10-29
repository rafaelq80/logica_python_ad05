import datetime
import calendar

# Nomes dos meses na mesma ordem usada pelo número do mês (janeiro = 1).
meses = [
  "janeiro", 
  "fevereiro", 
  "março", 
  "abril", 
  "maio", 
  "junho",
  "julho", 
  "agosto", 
  "setembro", 
  "outubro", 
  "novembro", 
  "dezembro"
]

# A função weekday() usa índices de 0 (segunda-feira) a 6 (domingo).
dias_semana = [
  "segunda-feira", 
  "terça-feira", 
  "quarta-feira", 
  "quinta-feira",
  "sexta-feira", 
  "sábado", 
  "domingo"
]

# Cria e exibe uma data específica: 21 de dezembro de 2024.
data = datetime.date(2024, 12, 21)
print(f"Data específica: {data}")

# Obtém a data atual e a exibe em formatos diferentes.
hoje = datetime.date.today()
print(f"Data atual: {hoje}")
print(f"Data atual (formato brasileiro): {hoje.strftime('%d/%m/%Y')}")

# Combina o dia da semana, o dia do mês, o nome do mês e o ano.
print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

# Verifica se 2024 é um ano bissexto.
print(f"2024 é Bissexto: {calendar.isleap(2024)}")

# monthrange(2026, 10) recebe o ano (2026) e o mês (10 = outubro);
# retorna o dia da semana do primeiro dia e a quantidade de dias do mês.
# O índice [1] seleciona a quantidade de dias, exibida pelo print.
print(f"Último dia do mês 10 (Outubro): {calendar.monthrange(2026, 10)[1]}")