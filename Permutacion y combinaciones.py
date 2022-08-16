from tkinter import *
from tkinter import ttk,font
from tkinter import messagebox

class ventana1: #clase principal para la ventana
    def __init__(self,ventana): #función para llamada principal
        self.venta=ventana #variable de la ventana
        self.venta.geometry("450x290") #tamaño de la ventana
        self.venta.resizable(width=0, height=0) #para evitar que se cambie el tamaño
        self.venta.title("Permutaciones y Combinaciones")#titulo
        self.fuente = font.Font(weight='bold') #fuente definida
        self.vmuestra=StringVar() #variable para la muestra
        self.vgrupo=StringVar() #variable para los grupos
        self.mensaje=StringVar() #mensaje para el resultado
        self.sel = IntVar() #variable para guardar el valor del radioboton

        #POO
        # --------------------------------------------------------------------------------------------
        #Título
        self.titulo = Label(self.venta, text="Elige la operacion",font=self.fuente)
        self.titulo.grid(row=0,column=0, sticky="w"+"e", columnspan = 4)
                        #row(fila),column(columna),sticky(espaciado segun direcciones),columnspan(usar varias columnas)
        #Opción para elegir operación
        self.pemutacionR= Radiobutton(self.venta,text="Permutación", variable= self.sel, value=1)
        self.pemutacionR.grid(row=1,column=0,columnspan = 2,sticky="e",ipadx=25)#ipadx = el tamaño del margen interno del objeto del eje X
        
        self.combinacionR = Radiobutton(self.venta, text="Combinación", variable=self.sel, value=2)
        self.combinacionR.grid(row=1,column=2,columnspan = 2,sticky="w",ipadx=25)

        #Entrada de valores
        self.label2=Label(self.venta,text="Muestra:").grid(row=2,column=0,sticky="e")
        self.muestra=Entry(self.venta,textvariable=self.vmuestra).grid(row=2,column=1,ipadx=5)

        self.label3=Label(self.venta,text="Grupo:").grid(row=2,column=2,sticky="e")
        self.grupos=Entry(self.venta,textvariable=self.vgrupo).grid(row=2,column=3,ipadx=5)

        #Se llama la función selección mediante el boton
        self.boton=Button(self.venta,text="Resultado",command=self.seleccion)
        self.boton.grid(row=3,column=3,pady=10,ipadx=25)#padxy=margen interno por direccion

        self.resultado=Label(self.venta,text="",borderwidth=2,relief="groove",textvariable=self.mensaje,height=1,width=8,font=self.fuente)
        self.resultado.grid(row=4,column=0,ipadx=175,ipady=50,padx=8, columnspan = 4)
        
        #Se llama a la funcíon limpiar mediante el boton1
        self.boton1=Button(self.venta,text="Limpiar",command=lambda:self.vaciar())
        self.boton1.grid(row=5,column=3,pady= 10,ipadx=28)
    #Lógica 
    # --------------------------------------------------------------------------------------------
    def factorial(self,num):#función para factorizar
        resl = 1
        if num == 0 :
            return (resl)
        else:
            for i in range(1, num + 1):
                resl = resl * i#multiplicar el rango
            return (resl)

    def permutacion(self):
        n=int(self.vmuestra.get())
        grup=int(self.vgrupo.get())
        if n == 0 and grup == 0:#comprobar las variables
            self.mensaje.set("Debe de ingresar valores mayores a cero.")
        else:#operacion de la permutación
            numerador = self.factorial(int(n))
            denominador = self.factorial((n - grup))
            resultado = numerador / denominador
            self.mensaje.set(float(resultado))

    def combinaciones(self):
        n=int(self.vmuestra.get())
        grup=int(self.vgrupo.get())
        if n == 0 and grup == 0:#comprobar las variables
            self.mensaje.set("Debe de ingresar valores mayores a cero.")
        else:#operacion de la combinaciones
            numerador = self.factorial(n)
            subdenomi1 = self.factorial(grup)
            subdenomi2 = self.factorial(n-grup)
            denominador = subdenomi1 * subdenomi2
            resultado = numerador/denominador
            self.mensaje.set(float(resultado))

    def seleccion(self):#función para escoger operación
        if self.sel.get() == 1:
            self.permutacion()
        elif self.sel.get() ==2:
            self.combinaciones()
        else:#Si estan vacios las barras de textos
            messagebox.showinfo(title="Problema con la ejecución ", message="Debio seleccionar si la operacion es una permutación o una combinación")

    def vaciar(self):#funcion para limpiar todas las variables
        self.vmuestra.set("")
        self.sel.set(None)
        self.vgrupo.set("")
        self.mensaje.set("")

if __name__ == '__main__':#condicional para ejecutar la ventana
    ventana = Tk()#Herramientas de tkinter
    w = ventana1(ventana)#clase
    ventana.mainloop()#Ejecutar la ventana en bucle







