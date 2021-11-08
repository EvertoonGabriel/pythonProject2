from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/loginPrestador.html")
def loginprestador():
    return render_template("loginprestador.html")

@app.route("/marcar.html")
def marcar():
    return render_template ("marcar.html")

@app.route ("/PaginadeConclusao.html")
def paginadeconclusao():
    return render_template("paginadeconclusao.html")

@app.route ("/PaginadeConclusao2.html")
def paginadeconclusao2():
    return render_template("paginadeconclusao2.html")

@app.route ("/PaginadeConclusaoPrestador.html")
def paginadeconclusaoprestador():
    return render_template("paginadeconclusaoprestador.html")

@app.route ("/preCadastro.html")
def precadastro():
    return render_template("precadastro.html")

if __name__ == "__main__":
    app.run(debug=True)

