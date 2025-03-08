import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cliente import Cliente



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

        
        def mensaje():
            if self.id.get() != "":
                
                if self.id.get() != "" and self.last_name.get() != "" and self.name.get() != "":
                    data = {
                        "id": self.id.get(),
                        "name": f"{self.name.get()}{self.last_name.get()}",
                        "frec_visit": 1,
                        "feedback": self.feedback.get()
                    }
                    cliente = Cliente(data)
                    cliente.register()
                else: 
                    messagebox.showinfo("Cleinte", "Debe llenar todos los campos")
            else:
                messagebox.showinfo("Cliente", "Nuevo Cliente")

        fr1 = tk.Frame(self.toplevel); fr1.pack(pady=10)
        fr2 = tk.Frame(self.toplevel); fr2.pack(pady=5)
        fr3 = tk.Frame(self.toplevel); fr3.pack(pady=5)
        fr4 = tk.Frame(self.toplevel); fr4.pack(pady=25)
        

        
       
        
        tk.Label(fr1, text="Cedula Del Cliente: ").pack(side="left")
        tk.Entry(fr1, textvariable=self.id).pack(side="left", padx=6)
        
        tk.Button(fr4, foreground=COLOR1, text="Añadir Cliente", relief="groove", width=20, height=2, font=("Inter Bold", 10), command=mensaje
        ).grid(column=0,row=0)
      

        
        Widget.InputGrid(fr2, "Nombre del cliente:", self.name, [0, 0], width=16)
        Widget.InputGrid(fr2, "Apellido del cliente:", self.last_name, [1, 0], width=16)
        
        Widget.CaptionGrid(fr3, "Comentario:", [0, 0])
        entryfeedback = tk.Entry(fr3, textvariable=self.feedback, font=("Inter", 10),width=30)
        entryfeedback.grid(column=0, row=3, ipady = 10)
        
        
        
        
class Sale(Form):
    def __init__(self, main_window):
        super().__init__(main_window, "Registro Cliente")
        
        
        
        

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Sistema Gestion - MeatFlow")
    ventana.geometry("1280x720")
    ventana.option_add("*Font", ("Inter", 10))
    ventana.withdraw()
    Client = Client(ventana)
    Client.show()
    ventana.mainloop()


