class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id_pro)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "id_pro": producto.id_pro,
                "nombre": producto.nom_pro,
                "acumulado": int(producto.pric_pro),
                "cantidad": 1,
            }
            #print("se agrego el producto")
            #print("id del producto" + str(self.carrito[id]["id_pro"]))
            #print("id_pro" + id)
        else:
            #print("se agrego el producto por segunda vez")
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += int(producto.pric_pro)
            #print("acumulado: " + str(self.carrito[id]["acumulado"]))
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id_pro)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id_pro)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= int(producto.pric_pro)
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

        

