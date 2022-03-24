import pyfirmata
import time
if __name__ == '__main__':
    # Inicializando comunicacion con arduino
    board = pyfirmata.Arduino('COM3')
    print("Comunicacion con arduino iniciada")
    
    # crear variables del boton y los led
    button = board.digital[4]
    LED1 = board.digital[13]
    LED2 = board.digital[8]
   
    LEDs = [LED1, LED2]
    LED_index = 0
    previous_button_state = 0
    
    # Iniciar iterador para recibir datos de entrada
    it = pyfirmata.util.Iterator(board)
    it.start()
    counter = 0
    last_status = False
    
    # configuraciion del boton
    button.mode = pyfirmata.INPUT
    
    def __init__(self, write, board):
        self.write = write
        self.board = board
    
        
    for LED in LEDs:
        LED.write(0)
    
    while True:
        # la velocidad con la que arranca el ciclo
        time.sleep(0.1)
            
        # obtencion del estado actual del boton
        button_state = button.read()       
             
        # configuracion del boton cuando se ha pulsado y cuando se ha soltado
        if button_state != previous_button_state:
            if button_state is True:
                if button_state != last_status:
                    counter += 1
                    if counter == 2:
                        print("Led Encendido")
                        LEDs[LED_index].write(1)
                        time.sleep(5)
                        print("Led Apagado")
                        LEDs[LED_index].write(0)
                        counter = 0
                        LED_index += 1
                        if LED_index > len(LEDs):
                            LED_index = 0
                
            
        # Guardar el estado actual del botón como anterior para la siguente iteracion del boton
        previous_button_state = button_state
        
        
