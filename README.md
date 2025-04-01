# hello-flask
# hello-flask

Introducción al desarrollo web con Python y Flask

## Nota a tener en cuenta

Flask necesita un servidor web para funcionar.
El servidor web es el encargado de recibir las peticiones
HTTP del navegador y enviarlas al programa que
hacemos en Flask. Flask le da el resultado al servidor
web y este se encarga de enviarlo al navegador.

Para simplificar el escenario, por el momento solamente
vamos a utilizar EL **SERVIDOR DE DESARROLLO** que nos
proporciona Flask. Este servidor **NO SIRVE para poner una
aplicación pública en internet en modo de PRODUCCIÓN**.
Solamente sirve en el escenario en el que estamos
desarrollando localmente nuestra aplicación.


## Variables de entorno

- Linux / Mac

```
export FLASK_APP=hola
export FLASK_DEBUG=True
```

- Windows

```
set FLASK_APP=hola
set FLASK_DEBUG=True
```

## Para lanzar la aplicación

1. Crear un entorno virtual, activarlo e instalar las
   dependencias

```
# Mac / Linux
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt

# Windows
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

2. Hacer una copia del archivo `.env_template` con
   el nombre `.env` y ajustar los valores (por ejemplo,
   activando el modo depuración)

3. Ejecutar la aplicación con el servidor de desarrollo

```
flask run
```


# Ciclo petición y respuesta

En la imagen se puede ver el flujo de peticiones y
datos para pintar la lista de movimientos usando Flask
y la plantilla `inicio.html` para verla en el
navegador.

![Petición y respuesta](./docs/ciclo-peticion-respuesta-flask.png)

# Documentos de referencia

- [Qué es internet](./docs/01%20-%20Qué%20es%20internet.pdf)
- [Introducción a la web: ciclo petición y respuesta](./docs/02%20-%20Intro%20web%20-%20petición%20y%20respuesta.pdf)
- [Introducción a HTML5](./docs/03%20-%20HTML5%20intro.pdf)
- [Resumen etiquetas HTML5](./docs/Resumen%20etiquetas%20HTML5.pdf)
