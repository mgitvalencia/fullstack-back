from persistencia import guardar_pedido

with open("pedidos.txt", "w", encoding="utf-8") as file:
 file.write("")
 file.close()

 pedidos = [{"nombre": "Pedro", "apellidos": "Gil deDiego"},
            {"nombre": "Michael", "apellidos": "Jordan"},
            {"nombre": "Mauricio", "apellidos": "Valencia"}]

for n in pedidos:
    guardar_pedido(n["nombre"],n["apellidos"])

