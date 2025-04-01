from flask import Flask


app = Flask('app-hola-flask')


@app.route('/')
def hola():
    return 'Hola, yo soy Flask'

@app.route('/adios')
def adios():
    return 'Te dejo, que tengo que irme'

@app.route('/nueva')
def cualquier_nombre():
    return 'Esta es una ruta nueva. Cuidado con los moradores de las arenas...'