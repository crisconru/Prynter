import serial
from serial.tools.list_ports import comports
import escpos


def select_device():
    print('Elegir impresora térmica:')
    i = 0
    devices = []
    for device in comports():
        print('{}) {} {} {}'.format(i, device.device, device.description,
                                    device.manufacturer))
        i += 1
        devices.append(device.device)
    opc = input()
    return devices[int(opc)]


class Prynter(serial.Serial):
    def __init__(self, port=None, baudrate=9600):
        super().__init__(port=port, baudrate=baudrate)
        print('Comunicacion abierta = {}'.format(self.is_open))

    def send(self, msg, rep=3):
        if rep:
            if self.is_open:
                self.write(msg)
                return True
            else:
                self.open()
                self.send(msg, rep-1)

    def initialization(self):
        msg = escpos.esc_command_dec('ESC', '@')
        if self.send(msg):
            print('Initialization send')
            #msg = escpos.esc_command_dec('ESC', '7', 7, 80, 2)
            #if self.send(msg):
            #    print('Adafruit configuration')
            #self.send(escpos.esc_command_dec('ESC', '7'))
            #self.send(escpos.esc_command_dec(7, 80, 2))

    def print(self, txt):
        msg = escpos.esc_command_dec(txt)
        if self.send(msg):
            print('Text send')
            self.line_feed()

    def line_feed(self):
        msg = escpos.esc_command_dec('LF')
        if self.send(msg):
            print('Line feed send')

    def bold_text(self, var=False):
        n = 1 if var else 0
        msg = escpos.esc_command_dec('ESC', '@', n)
        if self.send(msg):
            print('Bold send')


if __name__ == '__main__':
    port = select_device()
    print('Seleccionado {}'.format(port))
    impresora = Prynter(port=port)
    opt = '9'
    while opt != '0':
        txt = input('1) Inicializar\n2) Hola mundo\n3) Line Feed\n4) Bold\n0) '
                    'Exit\n')
        if txt == '1':
            impresora.initialization()
        elif txt == '2':
            impresora.print('Hola mundo')
            # impresora.line_feed()
        elif txt == '3':
            impresora.line_feed()
        elif txt == '4':
            impresora.bold_text(True)
        else:
            opt = '9' if txt != '0' else '0'
