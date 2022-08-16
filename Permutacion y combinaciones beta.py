from tkinter import *
from tkinter import font
from tkinter import messagebox


class estadistica_CP:
    def __init__(self, ventana):
        self.ventanafirst = ventana
        self.ventanafirst.title("Permutaciones & Combinaciones")
        self.fuente = font.Font(weight='bold')
        self.ventanafirst.resizable(0,0)

        self.n = StringVar()
        self.r = StringVar()
        self.resultado = IntVar()
        self.token_B = IntVar()

        self.resultado.set(0)
        self.token_B.set(1)
        self.validatecommand = self.ventanafirst.register(self.is_valid_char)

        self.combinacion_op = Radiobutton(self.ventanafirst, variable=self.token_B, value=1,text="Combinación").grid(row=0,column=1, sticky="w")
        self.permutacion_op = Radiobutton(self.ventanafirst, variable=self.token_B, value=2,text="Permutación").grid(row=0,column=3, sticky="w")
        
        self.label1 = Label(self.ventanafirst,font=self.fuente,text="Número de elementos" ).grid(row=1,column=1, sticky="w")
        self.barra_permu = Entry(self.ventanafirst, bg="black", fg="green", font =self.fuente, justify="left", textvariable= self.n, validate="key", validatecommand=(self.validatecommand, "%S"))
        self.barra_permu.grid(row=1,column=2, sticky="w", columnspan=4)

        self.label2 = Label(self.ventanafirst,font=self.fuente,text="Orden de elementos").grid(row=2,column=1, sticky="w")
        self.barra_combi = Entry(self.ventanafirst, bg="black", fg="green", font =self.fuente, justify="left", textvariable= self.r,validate="key", validatecommand=(self.validatecommand, "%S"))
        self.barra_combi.grid(row=2,column=2, sticky="w", columnspan=4)

        self.calcular= Button(self.ventanafirst, text="Calcular", font=self.fuente, command = lambda :self.formula(self.n.get(),self.r.get(),self.token_B.get()))
        self.calcular.grid(row=3,column=4, sticky="w"+"e")

    def factorial(self,num):
        resl = 1
        for i in range(1, num + 1):
            resl = resl * i
        return (resl)

    def formula(self,n,r,token):
            verficar = self.verificar(n, r)
            if verficar == False: 
                numerador= self.factorial(int(n))
                subdenomi1= self.factorial(int(r))
                subdenomi2 = self.factorial(int(n)-int(r))

                if token == 1: 
                    denominador=subdenomi1 * subdenomi2
                elif token == 2: 
                    denominador= subdenomi2
                resultado= numerador/denominador
                print(messagebox.showinfo(message="El resultado es: "+str(resultado), title="RESULTADO"))
            else:
                print(messagebox.showinfo(message="Debe de ingresar números", title="Aviso"))  
            self.n.set("")
            self.r.set("")


    def verificar(self,n,r):
        ver = False
        if self.n.get() == "" or self.r.get() == "": 
            ver = True
        return ver
            

    def is_valid_char(self,char):
        return char in "0123456789."

if __name__ == '__main__':
    ventana = Tk()
    ventanaloop = estadistica_CP(ventana)
    ventana.mainloop()
