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
        self.initialization()

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
            # self.adafruit()

    def adafruit(self):
            msg = escpos.esc_command_dec('ESC', '7', 7, 80, 2)
            if self.send(msg):
                print('Adafruit configuration')

    def print(self, txt):
        msg = escpos.esc_command_dec(txt)
        if self.send(msg):
            print('Text send')
            self.line_feed()

    def line_feed(self, n=1):
        msg = escpos.esc_command_dec('LF')
        for i in range(n):
            if self.send(msg):
                print('Line feed send')

    def justify(self, align="L"):
        # ESC a n | n = 0 LEFT, 1 CENTER,  2 RIGHT
        alignment = {'L': 0, 'C': 1, 'R': 2}
        pos = alignment[align] if align in alignment else 0
        msg = escpos.esc_command_dec('ESC', 'a', pos)
        if self.send(msg):
            print('Justify {} send'.format(align))

    def bold_text(self, n=0):
        # n = 1 BOLD | n = 0 NORMAL
        msg = escpos.esc_command_dec('ESC', 'E', n)
        if self.send(msg):
            print('Bold send')

    def cut(self):
        msg = escpos.esc_command_dec(29, 86, 48)
        if self.send(msg):
            print('Cut send')

    def test(self):
        self.justify('C')
        self.print('Centro')
        #self.line_feed()
        self.justify('R')
        self.bold_text(1)
        self.print('Derecha negra')
        #self.line_feed()
        self.justify()
        self.bold_text(0)
        self.print('Izquierda normal')
        #self.line_feed()
        self.print('tocame el pollonazo hijo de mil putas me caguen dios hijo de mordor')
        self.cut()
        self.print('\n\n')


if __name__ == '__main__':
    port = select_device()
    print('Seleccionado {}'.format(port))
    impresora = Prynter(port=port)
    opt = '9'
    while opt != '0':
        txt = input('0) Salir\n1) Inicializar\n2) Hola mundo\n3) Line Feed\n'
                    '4) Negrita\n5) Test\n')
        if txt == '1':
            impresora.initialization()
        elif txt == '2':
            impresora.print('Hola mundo')
            # impresora.line_feed()
        elif txt == '3':
            impresora.line_feed(6)
        elif txt == '4':
            impresora.bold_text(True)
        elif txt == '5':
            impresora.test()
        else:
            opt = '9' if txt != '0' else '0'
