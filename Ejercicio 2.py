from tkinter import *
from tkinter import ttk
import serial, time

arduino = serial.Serial("COM3", 9600)
print("Comunicacion con arduino iniciada")
#crear una instancia de tkinter frame
win= Tk()

#definir tamaño de la ventana
win.geometry("750x250")

#funciones a utilizar
def encenderled(e):
   print("Doble Click, Led Encendido")
   arduino.write(b'1')
   time.sleep(10)
   print("Led Apagado")

def close_window ():
    win.destroy()

#Define el titulo de la ventana
Label(win, text= "Enceder LED con Doble Click",font=('Helvetica 15 underline')).pack(pady=30)

#definir color y estilo del boton
ttk.Style().configure("TButton", padding=6, relief="flat", background="#000")

#Crear botones
ttk.Button(win, text= "Enceder LED", command=lambda:encenderled).pack(pady=20)
ttk.Button(win, text= "Salir", command=close_window).pack(pady=20)

#Enlazar el doble clic con el controlador
win.bind('<Double-Button-1>', encenderled)

#cambiar color de la ventana
win['bg'] = 'red'
win.mainloop()