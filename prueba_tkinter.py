import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cliente import Cliente
from handledb import DB



COLOR1 = "#225270"
COLOR1_SOFT = "#C4DDED"

class Widget:
    @staticmethod
    def MainLabel(parent, text):
        tk.Label(parent, text=text,foreground=COLOR1, font=("Inter ExtraBold", 24)
        ).pack(padx=90, pady=(30, 0))

    @staticmethod
    def SecLabel(parent, text):
        tk.Label(parent, text=text, font=("Inter", 10)
        ).pack()

    @staticmethod
    def Caption(parent, text):
        tk.Label(parent, text=text, foreground=COLOR1, font=("Inter SemiBold", 10)
        ).pack()
    
    @staticmethod
    def CaptionGrid(parent, text, arr, cspan=1, rspan=1):
        tk.Label(parent, text=text, foreground=COLOR1, font=("Inter SemiBold", 10)
        ).grid(column=arr[0], row=arr[1], columnspan=cspan, rowspan=rspan, sticky="w")

    @staticmethod
    def Input(parent, text, var, fs=11):
        Widget.Caption(parent, text)
        tk.Entry(parent, textvariable=var, font=("Inter", fs)
        ).pack()

    @staticmethod
    def InputGrid(parent, text, var, arr, cspan=1, rspan=1, width=None, fs=11):
        fr = tk.Frame(parent)
        Widget.CaptionGrid(fr, text, arr, cspan, rspan)
        et = None
        if width:
            et = tk.Entry(fr, textvariable=var, font=("Inter", fs), width=width)
        else:
            et = tk.Entry(fr, textvariable=var, font=("Inter", fs))

        et.grid(column=arr[0], row=(arr[1]+1), columnspan=cspan, rowspan=rspan)
        fr.grid(column=arr[0], row=arr[1], padx=8)

class Form:
    def __init__(self, main_window, title):
        self.main_window = main_window
        self.toplevel = tk.Toplevel(main_window)
        self.toplevel.title(f"{title} - MeatFlow")
        Widget.MainLabel(self.toplevel, title)
        self.toplevel.withdraw()  # Inicialmente oculto
        self.toplevel.resizable(False, False)


        self.toplevel.protocol("WM_DELETE_WINDOW", self.handleQuit)

    def show(self):
        self.toplevel.deiconify()  # Mostrar el formulario

    def hide(self):
        self.toplevel.destroy()  # Mostrar el formulario

    #- NOTA: ESTE METODO ES SOLO PARA EL <<LOGINFORM>>, CAMBIARLO ANTES DE PRODUCC
    def handleQuit(self):
        self.toplevel.destroy()
        self.main_window.destroy()
"""
Cliente debe de tener:
    Nombre: ---->Str
    Apellido
    Id: (Cedula) ---> Str
    Comentario: (?) ----- Str
    
"""
class Client(Form):
    def __init__(self, main_window):
        super().__init__(main_window, "Registro Cliente")
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.id = tk.StringVar()
        self.feedback = tk.StringVar()

        
        def validar_cliente():
            result = DB.getOneBy("clientes", "id", self.id.get())
            if result != None and self.id.get() == result["id"]:
                name, last_name = result["name"].split(" ",1)
                self.name.set(name)
                self.last_name.set(last_name)
                self.feedback.set("")
                return False
            else:
                return True
        
        def registrar():
            if validar_cliente():
                if self.id.get() != "" and self.last_name.get() != "" and self.name.get() != "":
                        data = {
                            "id": self.id.get(),
                            "name": f"{self.name.get()} {self.last_name.get()}",
                            "frec_visit": 1,
                            "feedback": self.feedback.get()
                        }
                        cliente = Cliente(data)
                        cliente.register()
                else: 
                    messagebox.showinfo("Cliente", "Debe llenar todos los campos")
            else:
                messagebox.showinfo("Cliente", "Cliente ya registrado")

        fr1 = tk.Frame(self.toplevel); fr1.pack(pady=10)
        fr2 = tk.Frame(self.toplevel); fr2.pack(pady=5)
        fr3 = tk.Frame(self.toplevel); fr3.pack(pady=5)
        fr4 = tk.Frame(self.toplevel); fr4.pack(pady=25)
        

        
       
        
        tk.Label(fr1, text="Cedula Del Cliente: ").pack(side="left")
        tk.Entry(fr1, textvariable=self.id).pack(side="left", padx=6)
        
        tk.Button(fr1, text="Ver Cliente", relief="groove", font=("Inter", 9), command = validar_cliente).pack(side="left")
      

        
        Widget.InputGrid(fr2, "Nombre del cliente:", self.name, [0, 0], width=16)
        Widget.InputGrid(fr2, "Apellido del cliente:", self.last_name, [1, 0], width=16)
        
        Widget.CaptionGrid(fr3, "Comentario:", [0, 0])
        entryfeedback = tk.Entry(fr3, textvariable=self.feedback, font=("Inter", 10),width=30)
        entryfeedback.grid(column=0, row=3, ipady = 10)
        tk.Button(fr4, foreground=COLOR1, text="Añadir Cliente", relief="groove", width=20, height=2, font=("Inter Bold", 10), command=registrar
        ).grid(column=0, row=0)
"""
Tiene:
Fecha = -----> String
Productos Vendidos = -----> list
Cliente = -------> Clase heredada
Metodo de pago = -------> String
Puntuacion Atencion = --------> Int
"""
class Sale(Form):
    def __init__(self, main_window, client: Client):
        super().__init__(main_window, "Orden de Venta")
        self.date = tk.StringVar()
        self.pay = tk.StringVar()
        self.attention = tk.IntVar()

        # Lista de productos comprados
        self.products_list = []

        self.name = client.name
        self.last_name = client.last_name
        
        fr1 = tk.Frame(self.toplevel); fr1.pack(pady=10)
        fr2 = tk.Frame(self.toplevel); fr2.pack(pady=5)
        

        
        # Mostrar el cliente
        tk.Label(fr1, text="Cliente:").pack(side="left")
        tk.Label(fr1, textvariable=self.name).pack(side="left", padx=5)
        tk.Label(fr1, textvariable=self.last_name).pack(side="left", padx=5)

        # Campos de entrada
        Widget.InputGrid(fr2, "Fecha:", self.date, [0, 0], width=16)
        Widget.InputGrid(fr2, "Método de pago:", self.pay, [1, 0], width=16)
        Widget.InputGrid(fr2, "Valoracion de atencion:", self.attention, [2, 0], width=16)

        # Sección de productos
        fr_products = tk.Frame(self.toplevel)
        fr_products.pack(pady=5)

        tk.Label(fr_products, text="Producto:").pack(side="left")
        self.product_entry = tk.Entry(fr_products, font=("Inter", 10))
        self.product_entry.pack(side="left", padx=5)

        tk.Label(fr_products, text="Cantidad:").pack(side="left")
        self.quantity_entry = tk.Entry(fr_products, font=("Inter", 10), width=5)
        self.quantity_entry.pack(side="left", padx=5)

        tk.Button(fr_products, text="Agregar", command=self.add_product).pack(side="left")

        # Caja de texto para mostrar productos agregados
        self.products_display = tk.Text(self.toplevel, height=10, width=40, state="disabled")
        self.products_display.pack(pady=10)
        fr_facturar = tk.Frame(self.toplevel); fr_facturar.pack(pady=25)
        tk.Button(fr_facturar, foreground=COLOR1, text="Facturar", relief="groove", width=20, height=2, font=("Inter Bold", 10), command=None
        ).grid(column=0, row=0)
        
    def add_product(self):
        """Agrega un producto con cantidad a la lista y lo muestra en la caja de texto."""
        product = self.product_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if product and quantity.isdigit() and int(quantity) > 0:
            product_entry = f"{product} x{quantity}"  # Formato "Jamón x2"
            self.products_list.append(product_entry)

            # Mostrar en la caja de texto
            self.products_display.config(state="normal")
            self.products_display.insert(tk.END, f"{product_entry}\n")
            self.products_display.config(state="disabled")

            # Limpiar los campos de entrada
            self.product_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            print("⚠️ Error: Ingresa un producto y una cantidad válida.") 
        
        
       
        
        
        
        
        

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Sistema Gestion - MeatFlow")
    ventana.geometry("1280x720")
    ventana.option_add("*Font", ("Inter", 10))
    ventana.withdraw()
    Client = Client(ventana)
    Client.show()
   

    # Crear una instancia de Sale con el cliente
    venta = Sale(ventana, Client)
    venta.show()
    ventana.mainloop()


