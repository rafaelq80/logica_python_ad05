# Importa datetime para obter a data e hora atuais.
from datetime import datetime

# Importa format_date para formatar datas com nomes localizados.
from babel.dates import format_date

# Obtém a data e hora atuais do computador.
hoje = datetime.today()

# Formata a data atual por extenso:
# - hoje: data que será formatada;
# - format='long': estilo longo, com o mês escrito por extenso;
# - locale='pt_BR': usa as convenções do português do Brasil.
data_extenso = format_date(hoje, format='long', locale='pt_BR')

# Exibe a data formatada.
print(data_extenso)