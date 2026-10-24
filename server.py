from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "index.html",
        titulo="Biblioteca Universitaria Central",
        mensaje="Un espacio para aprender, investigar y descubrir.",
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        titulo="Catálogo",
        mensaje="Explora los materiales disponibles para apoyar tu aprendizaje.",
    )


@app.route("/servicios")
def servicios():
    return render_template(
        "servicios.html",
        titulo="Servicios",
        mensaje="Conoce los servicios que ponemos a tu disposición.",
    )


@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        titulo="Contacto",
        mensaje="Estamos aquí para ayudarte. Comunícate con la biblioteca.",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5050)