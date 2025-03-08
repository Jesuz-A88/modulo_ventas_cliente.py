from cliente import Cliente
import datetime

class Venta:
    def __init__(self, client:Cliente, method, rate):
        self.date = datetime.datetime.now()
        self.client = client
        self.method_paid = method
        self.rate_sell = rate
    
    def __repr__(self):
        return f"Fecha: {self.date}\nCliente:\n CI: {self.client.id}\n Nombre: {self.client.name}\n Visitas: {self.client.frec_visit}\n Comentario: {self.client.feedback}\nMetodo de pago: {self.method_paid}\nMonto: {self.rate_sell}"

datos = {
    "id": 29554133,
    "name": "Henrry Aguey",
    "frec_visit": 1,
    "feedback": "Hola es la primera vez que vengo esta bonito el lugar"
}        


cliente = Cliente(datos)

venta = Venta(client=cliente, method="Tarjeta Credito", rate=2000)
print(venta)

