from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

print("hoy es {}".format(datetime.now().strftime("%A %d %b %Y")))