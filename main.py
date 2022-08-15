from threading import Thread
from tkinter import Tk, Button, Label
from gpiohelper import Proyecto_Domotica
from time import sleep

# Aqui se define todo lo de proyecto domotica
pc = Proyecto_Domotica()
pc.mandar_mensaje = False

pc.led1.nombre = 'Sala'
pc.led2.nombre = 'Cocina'
pc.led3.nombre = 'Recamara'

# Aqui se define todo lo de la UI
window = Tk()
fuente = "Helvetica 25 bold"
window.geometry('800x480')
autores = "Autores:\n@R-V-L"
window.attributes("-fullscreen", True)

# Se crea un grid 2x6
for i in range(3):
    window.rowconfigure(i, weight=1)

for i in range(2):
    window.columnconfigure(i, weight=1, uniform="group1")

# Se define funcion para generar botones
def boton(LED, tipo):
    if LED == 'LED1':
        pcLED = pc.led1
        pcLED.nombre = 'Recamara'
    elif LED == 'LED2':
        pcLED = pc.led2
        pcLED.nombre = 'Sala'
    elif LED == 'LED3':
        pcLED = pc.led3
        pcLED.nombre = 'Baño'

    if tipo == 'encender':
        texto = f"Encender {pcLED.nombre}"
        color = 'green'
        boton = Button(window, text=texto, font=fuente,
                       bg=color, fg="white", command=lambda: pc.encender_led(pcLED))
    else:
        texto = f"Apagar {pcLED.nombre}"
        color = 'darkred'
        boton = Button(window, text=texto, font=fuente,
                       bg=color, fg="white", command=lambda: pc.apagar_led(pcLED))
    return boton

boton1 = boton('LED1', 'encender').grid(row=0, column=0, sticky="NESW")
boton2 = boton('LED1', 'apagar').grid(row=0, column=1, sticky="NESW")
boton3 = boton('LED2', 'encender').grid(row=1, column=0, sticky="NESW")
boton4 = boton('LED2', 'apagar').grid(row=1, column=1, sticky="NESW")
boton5 = boton('LED3', 'encender').grid(row=2, column=0, sticky="NESW")
boton6 = boton('LED3', 'apagar').grid(row=2, column=1, sticky="NESW")

autores = Label(window, text=autores, bg='black', fg='white', font="Helvetica 10 bold")
autores.grid(row=3, column=0, columnspan=2, sticky="ew")

def rfid_leer():
    while True:
        if pc.lector_rfid():
            pc.buzzer.beep(on_time=0.2, off_time=0.2, n=2)
            sleep(0.2)
        pc.pir.when_line = lambda: pc.buzzSwitch(pc.buzzer, 'on')
        pc.pir.when_no_line = lambda: pc.buzzSwitch(pc.buzzer, 'off')
        sleep(0.3)

Thread(target=rfid_leer).start()
print("Proyecto Iniciado")

window.mainloop()