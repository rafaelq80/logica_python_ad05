from datetime import datetime
from babel.dates import format_date

hoje = datetime.today()
data_extenso = format_date(hoje, format='long', locale='pt_BR')
print(data_extenso)