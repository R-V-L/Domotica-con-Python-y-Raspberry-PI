from gpiozero import LED, LineSensor, Buzzer
from threading import Thread
from tghelper import mandar_mensaje
import logging
from mfrc522 import SimpleMFRC522

logging.basicConfig(level = logging.INFO,
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class Proyecto_Domotica():
    def __init__(self):
        setattr(LED, 'nombre', '')
        self.buzzer = Buzzer(20)
        self.buzzer.off()

        self.led1 = LED(6)
        self.led1.nombre = "Recamara"

        self.led2 = LED(13)
        self.led2.nombre = "Sala"

        self.led3 = LED(19)
        self.led3.nombre = "Baño"

        self.led4 = LED(26)
        self.led4.nombre = "Patio"
        
        self.pir = LineSensor(21)        
        self.reader = SimpleMFRC522()

        self.mandar_mensaje = True

    def buzzSwitch(self, buzzer, estado):
        if estado.lower() == 'on':
            buzzer.on()
            mensaje = "Alerta: Se detecto intruso"
            logging.info(mensaje)
            self.insertar_info(mensaje)
        elif estado.lower() == 'off':
            buzzer.off()
            mensaje = "Se dejo de detectar movimiento"
            logging.info(mensaje)
            self.insertar_info(mensaje)

    def encender_led(self, led):
        if not led.is_lit:
            led.on()
            mensaje = f"LED: {led.nombre}, Estatus: Encendido"
            logging.info(mensaje)
            self.insertar_info(mensaje)
        else:
            logging.error("{led.nombre} ya esta encendido")

    def apagar_led(self, led):
        if led.is_lit:
            led.off()
            mensaje = f"LED: {led.nombre}, Estatus: Apagado"
            logging.info(mensaje)
            self.insertar_info(mensaje)
        else:
            logging.error("{led.nombre} ya esta encendido")
         
    def lector_rfid(self):
        id = self.reader.read_id_no_block()
        if id == 207396674731:
            mensaje = "ID detectado: Ricardo, Acceso otorgado"
            logging.info(mensaje)
            self.insertar_info(mensaje)
            return True
        elif id == 494742417792:
            mensaje = "ID detectado: Pablo, Acceso otorgado"
            logging.info(mensaje)
            self.insertar_info(mensaje)
            return True
        elif id == None:
            pass
        else:
            mensaje = "ID no reconocido, Acceso denegado."
            logging.warning(mensaje)

        if id != None:
            self.insertar_info(mensaje)

    def insertar_info(self, mensaje):
        if self.mandar_mensaje:
            Thread(target=mandar_mensaje, args=(mensaje,)).start()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    from time import sleep
    pc = Proyecto_Domotica()
    pc.mandar_mensaje = True
    pc.encender_led(pc.led4)
    sleep(100)