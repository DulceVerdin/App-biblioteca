# Proyecto: Biblioteca Universitaria Central

Guía paso a paso para crear un sitio web informativo de una biblioteca
universitaria con **Python**, **Flask**, **Jinja2** y **Bootstrap**.

## 1. Crear la carpeta del proyecto

Abre PowerShell y crea la carpeta. Si ya tienes abierto este proyecto, puedes
continuar con el siguiente paso.

```powershell
mkdir biblioteca_universitaria
cd biblioteca_universitaria
```

## 2. Crear y activar un entorno virtual

El entorno virtual mantiene las dependencias del proyecto separadas de las
demás instalaciones de Python.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, puedes ejecutar los comandos siguientes
usando directamente `.\.venv\Scripts\python.exe` y
`.\.venv\Scripts\pip.exe`.

## 3. Instalar Flask

Instala Flask en el entorno virtual:

```powershell
pip install Flask
```

Guarda las dependencias del proyecto en `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

## 4. Crear la estructura del proyecto

Crea la carpeta `templates` y los archivos de la aplicación:

```text
biblioteca_universitaria/
├── server.py
├── requirements.txt
└── templates/
    ├── layout.html
    ├── index.html
    ├── catalogo.html
    ├── servicios.html
    └── contacto.html
```

Desde PowerShell puedes crear la carpeta de plantillas con:

```powershell
New-Item -ItemType Directory -Force templates
```

## 5. Programar las rutas de Flask

En `server.py`, importa `Flask` y `render_template`, crea la aplicación y define
una ruta para cada página. Cada función renderiza su plantilla y envía, como
mínimo, las variables `titulo` y `mensaje`.

Las rutas que debe ofrecer la aplicación son:

| Página | Ruta | Plantilla |
| --- | --- | --- |
| Inicio | `/` | `index.html` |
| Catálogo | `/catalogo` | `catalogo.html` |
| Servicios | `/servicios` | `servicios.html` |
| Contacto | `/contacto` | `contacto.html` |

Al final de `server.py`, inicia el servidor en el puerto `5050` para ejecutarlo
localmente:

```python
if __name__ == "__main__":
    app.run(debug=True, port=5050)
```

## 6. Crear la plantilla base

En `templates/layout.html`, define la estructura común de las páginas:

1. Escribe la estructura HTML e indica que el documento está en español.
2. Agrega el enlace a la hoja de estilos de Bootstrap.
3. Define el título del documento usando la variable `titulo`.
4. Agrega una barra de navegación horizontal con el nombre de la biblioteca y
   los enlaces **Inicio**, **Catálogo**, **Servicios** y **Contacto**.
5. Genera los destinos de los enlaces con `url_for()` usando los nombres de las
   funciones de las rutas.
6. Coloca el bloque `{% block content %}{% endblock %}` dentro de un elemento
   con la clase `container-fluid`.

La barra de navegación se define solamente en esta plantilla para que aparezca
automáticamente en todas las páginas.

## 7. Crear las páginas hijas

Crea cada plantilla en `templates/`. Todas deben extender la plantilla base y
colocar el contenido particular dentro del bloque `content`. Por ejemplo:

```html
{% extends "layout.html" %}

{% block content %}
  <h1>{{ titulo }}</h1>
  <p>{{ mensaje }}</p>
{% endblock %}
```

Incluye el contenido solicitado en cada página:

- **`index.html` (Inicio):** nombre de la biblioteca, bienvenida, propósito y
  horario general.
- **`catalogo.html` (Catálogo):** mensaje introductorio y descripción de libros,
  revistas, tesis y recursos digitales.
- **`servicios.html` (Servicios):** mensaje introductorio y descripción del
  préstamo de libros, consulta en sala, acceso a recursos digitales y
  orientación bibliográfica.
- **`contacto.html` (Contacto):** mensaje introductorio, dirección, correo
  institucional y horario. Usa datos ficticios o autorizados.

## 8. Ejecutar el proyecto

Desde la carpeta del proyecto y con el entorno virtual activado, instala las
dependencias (si todavía no lo hiciste) e inicia la aplicación:

```powershell
pip install -r requirements.txt
py server.py
```

Abre `http://127.0.0.1:5050` en el navegador. También puedes visitar
`http://127.0.0.1:5050/catalogo`, `http://127.0.0.1:5050/servicios` y
`http://127.0.0.1:5050/contacto`.

## 9. Verificar el funcionamiento

- Comprueba que las cuatro páginas carguen sin errores.
- Usa cada enlace del menú y confirma que abra la página correspondiente.
- Verifica que cada página muestre su título y mensaje.
- Confirma que el contenido específico de cada página esté presente.
- Asegúrate de que las páginas hijas hereden la navegación desde `layout.html`.

## 10. Publicar el proyecto en GitHub

Cuando tengas un repositorio remoto, agrega su URL aquí:

**URL de GitHub:** _agregar la URL del repositorio publicado_
