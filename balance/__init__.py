import os

from flask import Flask


RUTA_FICHERO = os.path.join('balance', 'data', 'movimientos.csv')

app = Flask(__name__)
app.config.from_prefixed_env()
print('El nombre de la APP en Flask es:', __name__)
print('APP', app.config.get('APP'))
print('DEBUG', app.config.get('DEBUG'))