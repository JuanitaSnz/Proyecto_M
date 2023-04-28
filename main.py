import tkinter

from numpy import character
from Simpson import simpson
from Secante import secante
from Punto_Fijo import punto
from Trapezoide import trapecio
from MBiseccion import biseccion
from Simpson import simpson

class MainWindow:
    def __init__(self):

        self.window=tkinter.Tk()
        self.window.title("Proyecto metodos")
        self.window.geometry("640x280")
        self.window.update()
        self.open_windows = []
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()

        x = int((screen_width / 2) - (self.window.winfo_width() / 2))
        y = int((screen_height / 2) - (self.window.winfo_height() / 2))

        self.window.geometry("+{}+{}".format(x, y))
        self.window.configure(background="darkgray")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.title = tkinter.Label(self.window, text="Bienvenido,elija el método con el que desea trabajar", bg="gold",font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.button1 = tkinter.Button(self.window,text="PUNTO FIJO", font="Helvetica 13", width=10, height=5, command=self.punto_fijo)
        self.button2 = tkinter.Button(self.window,text="BISECCIÓN", font="Helvetica 13", width=10, height=5,command=self.biseccion)
        self.button3 = tkinter.Button(self.window,text="SECANTE", font="Helvetica 13", width=10, height=5,command=self.secante)
        self.button4 = tkinter.Button(self.window,text="TRAPECIO", font="Helvetica 13", width=10, height=5,command=self.trapecio)
        self.button5 = tkinter.Button(self.window,text="SIMPSON", font="Helvetica 13", width=10, height=5,command=self.simpson)
        self.button6 = tkinter.Button(self.window,text="GAUSS-SEIDEL", font="Helvetica 13", width=10, height=5,command=self.gauss)

        self.button1.grid(row=1, column=0, padx=5, pady=5, sticky="NSEW")
        self.button2.grid(row=1, column=1, padx=5, pady=5, sticky="NSEW")
        self.button3.grid(row=1, column=2, padx=5, pady=5, sticky="NSEW")
        self.button4.grid(row=2, column=0, padx=5, pady=5, sticky="NSEW")
        self.button5.grid(row=2, column=1, padx=5, pady=5, sticky="NSEW")
        self.button6.grid(row=2, column=2, padx=5, pady=5, sticky="NSEW")

        for btn in (self.button1, self.button2, self.button3, self.button4, self.button5, self.button6):
            btn.configure(height=5, width=10)
        self.window.protocol("WM_DELETE_WINDOW", self.on_cerrar_ventana_principal)

    def on_cerrar_ventana_principal(self):
        self.window.destroy()

    def punto_fijo(self):
        self.window.withdraw()
        self.windowpt = tkinter.Toplevel(self.window)
        self.windowpt.title("Punto Fijo")
        self.windowpt.geometry("490x330")
        self.windowpt.configure(background="darkgray")
        #CENTRAR LA VENTANA EN LA PANTALLA
        self.windowpt.update()
        screen_width = self.windowpt.winfo_screenwidth()
        screen_height = self.windowpt.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowpt.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowpt.winfo_height() / 2))
        self.windowpt.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowpt, text="Metodo Punto Fijo", bg="gold", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
       #MENSAJE INFORMATIVO
        self.text = tkinter.Text(self.windowpt, width=68,height=4,font="Helvetica 10",state="disabled",bg="lightblue")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2)\n"
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0,columnspan=3, padx=3, pady=3)
        #FUNCION SIN DESPEJAR
        self.label_function=tkinter.Label(self.windowpt, text="Función sin despejar f(x):", font="Helvetica 13", background="darkgray")
        self.label_function.grid(row=2,column=0,padx=3, pady=3)
        self.entry_functionpt=tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_functionpt.grid(row=2,column=1,padx=3, pady=3)
        #FUNCION DESPEJADA
        self.label_gfunction = tkinter.Label(self.windowpt, text="Función despejada g(x):", font="Helvetica 13", background="darkgray")
        self.label_gfunction.grid(row=3, column=0,columnspan=1,padx=3, pady=3)
        self.entry_gfunction = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_gfunction.grid(row=3, column=1,padx=3, pady=3)
        #INGRESO INTERVALO a
        self.label_x0 = tkinter.Label(self.windowpt, text="Valor inicial X0:", font="Helvetica 13", background="darkgray")
        self.label_x0.grid(row=4, column=0, padx=3, pady=3)
        self.entry_apt = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_apt.config(validate="key")
        self.entry_apt.config(validatecommand=(self.entry_apt.register(self.validate), '%S'))
        self.entry_apt.grid(row=4, column=1, padx=3, pady=3)
        #PORCENTAJE DE ERROR
        self.label_err = tkinter.Label(self.windowpt, text="Ingrese el valor del error:", font="Helvetica 13", background="darkgray")
        self.label_err.grid(row=5, column=0,padx=3, pady=3)
        self.entry_errapt = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_errapt.config(validate="key")
        self.entry_errapt.config(validatecommand=(self.entry_errapt.register(self.validate), '%S'))
        self.entry_errapt.grid(row=5, column=1,padx=3, pady=3)
        #NUMERO MAXIMO DE ITERACIONES
        self.label_it = tkinter.Label(self.windowpt, text="Ingrese el maximo de iteraciones:", font="Helvetica 13", background="darkgray")
        self.label_it.grid(row=6, column=0,padx=3, pady=3)
        self.entry_it = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_it.config(validate="key")
        self.entry_it.config(validatecommand=(self.entry_it.register(self.validate), '%S'))
        self.entry_it.grid(row=6, column=1,padx=3, pady=3)
        #REGRESAR AL INICIO
        back_main = tkinter.Button(self.windowpt, text="Regresar", width=10, height=2, command=lambda:self.back(self.windowpt))
        back_main.grid(row=8, column=0,padx=10, pady=10)
        #CALCULAR
        calculate = tkinter.Button(self.windowpt, text="Calcular", width=10, height=2,command=self.startPuntoFijo)
        calculate.grid(row=8,column=1,padx=10, pady=10)
        self.open_windows.append(self.windowpt)

    def startPuntoFijo(self):
        punto(self.entry_functionpt.get(),self.entry_gfunction.get(),self.entry_apt.get(),self.entry_errapt.get(),self.entry_it.get())

    def biseccion(self):
        self.window.withdraw()
        self.windowbis=tkinter.Toplevel(self.window)
        self.windowbis.title("Biseccion")
        self.windowbis.geometry("405x265")
        self.windowbis.configure(background="darkgray")
        self.windowbis.update()
        screen_width = self.windowbis.winfo_screenwidth()
        screen_height = self.windowbis.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowbis.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowbis.winfo_height() / 2))
        self.windowbis.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowbis, text="Metodo Biseccion", bg="gold",font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.text = tkinter.Text(self.windowbis, width=56, height=4, font="Helvetica 10", state="disabled",bg="lightblue")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2)\n"
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)
        # FUNCION FX
        self.label_function = tkinter.Label(self.windowbis, text="Función  f(x):", font="Helvetica 13",background="darkgray")
        self.label_function.grid(row=2, column=0, columnspan=1, padx=3, pady=3)
        self.entry_functionbis = tkinter.Entry(self.windowbis, font="Helvetica 14")
        self.entry_functionbis.grid(row=2, column=1, padx=3, pady=3)
        # INGRESO INTERVALO a
        self.label_x0 = tkinter.Label(self.windowbis, text="Valor a intervalo [a,b]:", font="Helvetica 13",
                                      background="darkgray")
        self.label_x0.grid(row=3, column=0, padx=3, pady=3)
        self.entry_x0bis = tkinter.Entry(self.windowbis, font="Helvetica 14")
        self.entry_x0bis.config(validate="key")
        self.entry_x0bis.config(validatecommand=(self.entry_x0bis.register(self.validate), '%S'))
        self.entry_x0bis.grid(row=3, column=1, padx=3, pady=3)
        # INGRESO INTERVALO b
        self.label_intervalBbis = tkinter.Label(self.windowbis, text="Valor b intervalo [a,b]:", font="Helvetica 13",background="darkgray")
        self.label_intervalBbis.grid(row=4, column=0, padx=3, pady=3)
        self.entry_intervalBbis = tkinter.Entry(self.windowbis, font="Helvetica 14")
        self.entry_intervalBbis.config(validate="key")
        self.entry_intervalBbis.config(validatecommand=(self.entry_intervalBbis.register(self.validate), '%S'))
        self.entry_intervalBbis.grid(row=4, column=1, padx=3, pady=3)

        #REGRESAR
        back_main = tkinter.Button(self.windowbis, text="Regresar", width=10, height=2,command=lambda: self.back(self.windowbis))
        back_main.grid(row=5, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowbis, text="Calcular", width=10, height=2,command=self.startBiseccion)
        calculate.grid(row=5, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowbis)

    def startBiseccion(self):
        self.windowbis.withdraw()
        self.windowresbis=tkinter.Toplevel(self.windowbis)
        self.windowresbis.title("Resultado Biseccion")
        self.windowresbis.geometry("427x230")
        self.windowresbis.configure(background="darkgray")
        self.windowresbis.update()
        screen_width = self.windowresbis.winfo_screenwidth()
        screen_height = self.windowresbis.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowresbis.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowresbis.winfo_height() / 2))
        self.windowresbis.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowresbis, text="Resultados", bg="gold", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.label_function = tkinter.Label(self.windowresbis, text="La raíz se encuentra en:", font="Helvetica 13",background="darkgray")
        self.label_function.grid(row=1, column=0, padx=3, pady=3)
        result = biseccion(self.entry_functionbis.get(), self.entry_x0bis.get(), self.entry_intervalBbis.get())[1]
        print(result)
        self.label_res = tkinter.Label(self.windowresbis, text=str(result), font="Helvetica 13",background="darkgray")
        self.label_res.grid(row=2, column=0, padx=3, pady=3)
        back_main = tkinter.Button(self.windowresbis, text="Regresar", width=10, height=2,command=lambda: self.back(self.windowresbis))
        back_main.grid(row=5, column=0, padx=10, pady=10)
        self.open_windows.append(self.windowresbis)
    def secante (self):
        self.window.withdraw()
        self.windowsec = tkinter.Toplevel(self.window)
        self.windowsec.title("Secante")
        self.windowsec.geometry("427x230")
        self.windowsec.configure(background="darkgray")
        self.windowsec.update()
        screen_width = self.windowsec.winfo_screenwidth()
        screen_height = self.windowsec.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowsec.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowsec.winfo_height() / 2))
        self.windowsec.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowsec, text="Metodo Secante", bg="gold", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        # INGRESO FUNCION
        self.label_function = tkinter.Label(self.windowsec, text="Función f(x):", font="Helvetica 13", background="darkgray")
        self.label_function.grid(row=1, column=0, padx=3, pady=3)
        self.entry_functionsec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_functionsec.grid(row=1, column=1, padx=3, pady=3)
        # INGRESOX0
        self.label_x0 = tkinter.Label(self.windowsec, text="Valor X0:", font="Helvetica 13", background="darkgray")
        self.label_x0.grid(row=2, column=0, padx=3, pady=3)
        self.entry_x0sec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_x0sec.config(validate="key")
        self.entry_x0sec.config(validatecommand=(self.entry_x0sec.register(self.validate), '%S'))
        self.entry_x0sec.grid(row=2, column=1, padx=3, pady=3)
        # INGRESOX1
        self.label_x1 = tkinter.Label(self.windowsec, text="Valor X1:", font="Helvetica 13", background="darkgray")
        self.label_x1.grid(row=3, column=0, padx=3, pady=3)
        self.entry_x1sec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_x1sec.config(validate="key")
        self.entry_x1sec.config(validatecommand=(self.entry_x1sec.register(self.validate), '%S'))
        self.entry_x1sec.grid(row=3, column=1, padx=3, pady=3)
        # PORCENTAJE DE ERROR
        self.label_err = tkinter.Label(self.windowsec, text="Ingrese el valor del error:", font="Helvetica 13", background="darkgray")
        self.label_err.grid(row=4, column=0, padx=3, pady=3)
        self.entry_errsec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_errsec.config(validate="key")
        self.entry_errsec.config(validatecommand=(self.entry_errsec.register(self.validate), '%S'))
        self.entry_errsec.grid(row=4, column=1, padx=3, pady=3)
        # REGRESAR AL INICIO
        back_main = tkinter.Button(self.windowsec, text="Regresar", width=10, height=2, command=lambda: self.back(self.windowsec))
        back_main.grid(row=5, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowsec, text="Calcular", width=10, height=2,command=self.startSecante)
        calculate.grid(row=5, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowsec)

    def startSecante(self):
        secante(self.entry_functionsec.get(),self.entry_x0sec.get(),self.entry_x1sec.get(),self.entry_errsec.get())

    def trapecio(self):
            self.window.withdraw()
            self.windowtrap = tkinter.Toplevel(self.window)
            self.windowtrap.title("Trapecio")
            self.windowtrap.geometry("480x220")
            self.windowtrap.configure(background="darkgray")
            self.windowtrap.update()
            screen_width = self.windowtrap.winfo_screenwidth()
            screen_height = self.windowtrap.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowtrap.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowtrap.winfo_height() / 2))
            self.windowtrap.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowtrap, text="Metodo Trapecio", bg="gold", font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            # INGRESO FUNCION
            self.label_function = tkinter.Label(self.windowtrap, text="Función f(x):", font="Helvetica 13", background="darkgray")
            self.label_function.grid(row=1, column=0, padx=3, pady=3)
            self.entry_functiontrap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
            self.entry_functiontrap.grid(row=1, column=1, padx=3, pady=3)
            # INGRESO INTERVALO a
            self.label_x0 = tkinter.Label(self.windowtrap, text="Valor a intervalo [a,b]:", font="Helvetica 13",background="darkgray")
            self.label_x0.grid(row=3, column=0, padx=3, pady=3)
            self.entry_x0trap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
            self.entry_x0trap.config(validate="key")
            self.entry_x0trap.config(validatecommand=(self.entry_x0trap.register(self.validate), '%S'))
            self.entry_x0trap.grid(row=3, column=1, padx=3, pady=3)
            # INGRESO INTERVALO b
            self.label_intervalB = tkinter.Label(self.windowtrap, text="Valor b intervalo [a,b]:", font="Helvetica 13",background="darkgray")
            self.label_intervalB.grid(row=4, column=0, padx=3, pady=3)
            self.entry_intervalBtrap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
            self.entry_intervalBtrap.config(validate="key")
            self.entry_intervalBtrap.config(validatecommand=(self.entry_intervalBtrap.register(self.validate), '%S'))
            self.entry_intervalBtrap.grid(row=4, column=1, padx=3, pady=3)
            #NUMERO DE TRAPECIOS
            self.label_ntrap = tkinter.Label(self.windowtrap, text="Ingrese el numero de trapecios:", font="Helvetica 13",background="darkgray")
            self.label_ntrap.grid(row=5, column=0, padx=3, pady=3)
            self.entry_ntrap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
            self.entry_ntrap.config(validate="key")
            self.entry_ntrap.config(validatecommand=(self.entry_ntrap.register(self.validate), '%S'))
            self.entry_ntrap.grid(row=5, column=1, padx=3, pady=3)
            # REGRESAR AL INICIO
            back_main = tkinter.Button(self.windowtrap, text="Regresar", width=10, height=2,command=lambda: self.back(self.windowtrap))
            back_main.grid(row=6, column=0, padx=10, pady=10)
            # CALCULAR
            calculate = tkinter.Button(self.windowtrap, text="Calcular", width=10, height=2,command=self.startTrapecio)
            calculate.grid(row=6, column=1, padx=10, pady=10)
            self.open_windows.append(self.windowtrap)

    def startTrapecio(self):
        trapecio(self.entry_functiontrap.get(), self.entry_x0trap.get(), self.entry_intervalBtrap.get(), self.entry_ntrap.get())
    def simpson(self):
            self.window.withdraw()
            self.windowsimp = tkinter.Toplevel(self.window)
            self.windowsimp.title("Simpson")
            self.windowsimp.geometry("480x220")
            self.windowsimp.configure(background="darkgray")
            self.windowsimp.update()
            screen_width = self.windowsimp.winfo_screenwidth()
            screen_height = self.windowsimp.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowsimp.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowsimp.winfo_height() / 2))
            self.windowsimp.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowsimp, text="Metodo Simpson", bg="gold", font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            # INGRESO FUNCION
            self.label_function = tkinter.Label(self.windowsimp, text="Función f(x):", font="Helvetica 13",background="darkgray")
            self.label_function.grid(row=1, column=0, padx=3, pady=3)
            self.entry_functionsim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
            self.entry_functionsim.grid(row=1, column=1, padx=3, pady=3)
            # INGRESO INTERVALO a
            self.label_x0 = tkinter.Label(self.windowsimp, text="Valor a intervalo [a,b]:", font="Helvetica 13",background="darkgray")
            self.label_x0.grid(row=3, column=0, padx=3, pady=3)
            self.entry_x0sim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
            self.entry_x0sim.config(validate="key")
            self.entry_x0sim.config(validatecommand=(self.entry_x0sim.register(self.validate), '%S'))
            self.entry_x0sim.grid(row=3, column=1, padx=3, pady=3)
            # INGRESO INTERVALO b
            self.label_intervalB = tkinter.Label(self.windowsimp, text="Valor b intervalo [a,b]:", font="Helvetica 13",background="darkgray")
            self.label_intervalB.grid(row=4, column=0, padx=3, pady=3)
            self.entry_intervalBsim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
            self.entry_intervalBsim.config(validate="key")
            self.entry_intervalBsim.config(validatecommand=(self.entry_intervalBsim.register(self.validate), '%S'))
            self.entry_intervalBsim.grid(row=4, column=1, padx=3, pady=3)
            # NUMERO DE TRAPECIOS
            self.label_ntrap = tkinter.Label(self.windowsimp, text="Ingrese el numero de trapecios:",font="Helvetica 13", background="darkgray")
            self.label_ntrap.grid(row=5, column=0, padx=3, pady=3)
            self.entry_ntrapsim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
            self.entry_ntrapsim.config(validate="key")
            self.entry_ntrapsim.config(validatecommand=(self.entry_ntrapsim.register(self.validate), '%S'))
            self.entry_ntrapsim.grid(row=5, column=1, padx=3, pady=3)
            # REGRESAR AL INICIO
            back_main = tkinter.Button(self.windowsimp, text="Regresar", width=10, height=2,command=lambda: self.back(self.windowsimp))
            back_main.grid(row=6, column=0, padx=10, pady=10)
            # CALCULAR
            calculate = tkinter.Button(self.windowsimp, text="Calcular", width=10, height=2,command=self.startSimpson)
            calculate.grid(row=6, column=1, padx=10, pady=10)
            self.open_windows.append(self.windowsimp)

    def startSimpson(self):
        simpson(self.entry_functionsim.get(),self.entry_x0sim.get(),self.entry_intervalBsim.get(),self.entry_ntrapsim.get())
    def gauss(self):
            self.window.withdraw()
            self.windowgauss = tkinter.Toplevel(self.window)
            self.windowgauss.title("Biseccion")
            self.windowgauss.geometry("640x280")
            self.windowgauss.update()
            screen_width = self.windowgauss.winfo_screenwidth()
            screen_height = self.windowgauss.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowgauss.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowgauss.winfo_height() / 2))
            self.windowgauss.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowgauss, text="Metodo Gauss-seidel", bg="gold", font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            back_main = tkinter.Button(self.windowgauss, text="Regresar", width=10, height=2, command=lambda: self.back(self.windowgauss))
            back_main.grid(row=2, column=1)
            self.open_windows.append(self.windowgauss)

    def back(self,actual_window):
       actual_window.destroy()
       self.open_windows.pop()

       if self.open_windows:
         previous_window= self.open_windows[-1]
         previous_window.update()
         previous_window.deiconify()
         previous_window.focus_set()
       else:
        self.window.update()
        self.window.deiconify()
        self.window.focus_set()

    def validate(self,character):
        return all(c.isdigit() or c == '.' or (c == '-' and i == 0) for i, c in enumerate(character))



main_window=MainWindow()
main_window.window.mainloop()
