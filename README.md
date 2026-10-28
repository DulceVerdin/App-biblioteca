1. Crear la carpeta del proyecto
Primero abrí PowerShell y creé una carpeta llamada biblioteca_universitaria, donde voy a guardar todos los archivos de mi proyecto.
mkdir biblioteca_universitaria
cd biblioteca_universitaria


2. Crear el entorno virtual
Creé un entorno virtual para mantener separadas las librerías que necesita mi proyecto y después lo activé.
py -m venv .venv
.\.venv\Scripts\Activate.ps1


3. Instalar Flask
Instalé Flask, que me permite crear una página web con Python. También guardé las dependencias en un archivo llamado requirements.txt.
pip install Flask
pip freeze > requirements.txt


4. Crear los archivos del proyecto
Creé el archivo server.py y la carpeta templates, donde guardé las páginas HTML que va a utilizar mi sitio web.

Mi estructura quedó así:
biblioteca_universitaria/
├── server.py
├── requirements.txt
└── templates/
    ├── layout.html
    ├── index.html
    ├── catalogo.html
    ├── servicios.html
    └── contacto.html


5. Programar las rutas
En el archivo server.py programé las rutas para que cada opción del menú abra su página correspondiente.
- / para Inicio.
- /catalogo para Catálogo.
- /servicios para Servicios.
- /contacto para Contacto.
También configuré el servidor para que funcione en el puerto 5050.
6. Crear la plantilla principal
En layout.html hice la estructura principal de la página. Agregué Bootstrap para darle estilo y una barra de navegación con los enlaces de Inicio, Catálogo, Servicios y Contacto.

Esta plantilla se comparte con todas las páginas para no tener que repetir el mismo menú.
7. Crear las páginas
Creé las cuatro páginas HTML y utilicé la plantilla principal para que todas tuvieran el mismo diseño.
- Inicio: agregué una bienvenida, el propósito de la biblioteca y su horario.
- Catálogo: incluí información sobre libros, revistas, tesis y recursos digitales.
- Servicios: describí los préstamos de libros, las consultas en sala y la orientación bibliográfica.
- Contacto: agregué una dirección, un correo institucional y el horario de atención con datos ficticios.
8. Ejecutar el proyecto
Instalé las dependencias necesarias y ejecuté el archivo principal para iniciar el servidor.
pip install -r requirements.txt
py server.py


Después abrí el navegador y entré a http://127.0.0.1:5050 para ver mi página web.
9. Revisar que funcione
Probé las cuatro páginas y comprobé que los enlaces del menú funcionaran correctamente, que apareciera el contenido de cada sección y que todas compartieran el mismo diseño.
10. Publicar en GitHub
Por último, puedo subir mi proyecto a GitHub para guardar el código y compartirlo.

