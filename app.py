"""Pruebas Backend"""

from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    """Guardas datos"""
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    print(nombre)
    print(apellido)
    guardar_pedido(nombre,apellido)
    return redirect("http://localhost/naxer/solicita_pedido.html", code=302)
    
@app.route("/checksize",methods=['POST'])
def checksize():
    """Validar disponibilidad"""
    tamano = request.form.get("tamano")
    mensaje = "Disponible"
    if tamano == "S":
       mensaje = "No Disponible"
    print(mensaje) 
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
