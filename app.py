"""Pruebas Backend"""
from flask import Flask, request, redirect
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    print(nombre)
    print(apellido)
    guardar_pedido(nombre,apellido)
    return redirect("http://localhost/naxer/solicita_pedido.html", code=302)
