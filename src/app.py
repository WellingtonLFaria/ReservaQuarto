from flask import Flask, render_template, redirect, request, flash
from quartos import Quartos
from reservas import Reservas

gquartos = Quartos()
greservas = Reservas()

app = Flask(__name__)
app.config["SECRET_KEY"] = "sreserva"

@app.route("/")
def index():
    return redirect("/quartos")

@app.route("/quartos")
def quartos():
    return render_template("quartos.html", pag="QUARTOS", quartos=gquartos.VerQuartos())

@app.route("/quartos/add", methods=["POST"])
def adicionar_quarto():
    try:
        numero_quarto = int(request.form["numero_quarto"])
        tamanho_quarto = int(request.form["tamanho_quarto"])
        diaria_preco = float(request.form["diaria_preco"])
        flash(gquartos.AdicionarQuarto(numero_quarto=numero_quarto, tamanho_quarto=tamanho_quarto, diaria_preco=diaria_preco))
    except ValueError:
        flash("Algum valor inválido informado!")
    return redirect("/quartos")

@app.route("/quartos/delete", methods=["POST"])
def deletar_quarto():
    try:
        flash(gquartos.RemoverQuarto(int(request.form["numero_quarto"])))
    except ValueError:
        flash("Valor inválido!")
    return redirect("/quartos")

@app.route("/reservas")
def reservas():
    disponiveis = [quarto["numero_quarto"] for quarto in gquartos.VerQuartos() if quarto["numero_quarto"] not in [reserva["numero_quarto"] for reserva in greservas.VerReservas()]]
    return render_template("reservas.html", pag="RESERVAS", disponiveis=disponiveis, reservas=greservas.VerReservas())

@app.route("/reservas/add")
def reservar_quarto():
    try:
        greservas.ReservarQuarto(numero_quarto=request.form["numero_quarto"], dias=request.form["dias"])
    except ValueError:
        flash("Algum valor inválido!")
    return redirect("/reservas")

@app.route("/<rota>")
def rota_inválida(rota):
    msg = f"""
    <div style="position: absolute;top: 50%;left: 50%;transform: translate(-50%,-50%);">
        <h1>A rota /{rota} não existe!</h1>
        <a href="/quartos" style="display: block;width: 100px;background-color: #404040;padding: 5px;color: white;border-radius: 5px;margin: auto;text-align: center;">Página inicial</a>
    </div>
    """
    return msg