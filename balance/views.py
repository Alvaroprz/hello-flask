from flask import render_template

from .models import ListaMovimientos
from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    print(lista)
    return render_template('inicio.html', movs=lista.movimientos)

@app.route('/nuevo')
def agregar_movimiento():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV.
    """
    return 'Agregar nuevo movimiento'

@app.route('/modificar')
def editar():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento'

@app.route('/borrar')
def eliminar():
    """
    Elimina un movimiento existente
    """
    return 'Borrar movimiento'
