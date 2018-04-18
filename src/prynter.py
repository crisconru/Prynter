from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE
from serial.tools.list_ports import comports
from escpos import ESCPOS


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


class Prynter(Serial):
    def __init__(self, port=None, printer='stp80'):
        super().__init__(port=port, baudrate=38400, bytesize=EIGHTBITS,
                         parity=PARITY_NONE, stopbits=STOPBITS_ONE,
                         dsrdtr=True)
        self.printer = printer
        self.port = port
        '''
        if printer == 'stp80':
            print('stp80')
            self.baudrate = 9600
            self.dsrdtr = True
        elif printer == 'adafruit':
            print('adafruit')
            self.baudrate = 9600
        elif printer == 'epson':
            print('epson')
            self.baudrate = 38400
            self.bytesize = EIGHTBITS
            self.parity = PARITY_NONE
            self.stopbits = STOPBITS_ONE
            self.dsrdtr = True
            self.rtscts = False
            self.xonxoff = None
        '''
        print('Comunicacion abierta = {}'.format(self.is_open))
        self.esc = ESCPOS()
        self.esc.encoding('ascii')
        self.initialization()

    def send(self, msg, rep=3):
        if rep:
            if self.is_open:
                self.write(msg)
                return True
            else:
                self.open()
                self.send(msg, rep-1)

    def receive(self):
        self.timeout = 5.0
        rx = self.readline().decode()
        print('recibido = {}'.format(rx))

    def initialization(self):
        msg = self.esc.ascii_command('ESC', '@')
        if self.send(msg):
            print('Initialization send')
            if self.printer == 'adafruit':
                self.adafruit()
            #elif self.printer != 'stp80':
            #    msg = self.esc.ascii_command('ESC', 'S')
            #    if self.send(msg):
            #        print('Inicializacion de impresora approx')

    def adafruit(self):
            msg = self.esc.ascii_command('ESC', '7', 7, 80, 2)
            if self.send(msg):
                print('Adafruit configuration')

    def print(self, txt):
        msg = self.esc.string_to_escpos(txt)
        if self.send(msg):
            print('{} send'.format(txt))
            self.line_feed()

    def line_feed(self, n=1):
        msg = self.esc.ascii_command('LF')
        [print('Line feed send') for i in range(n) if self.send(msg)]

    def justify(self, align="L"):
        # ESC a n | n = 0 LEFT, 1 CENTER,  2 RIGHT
        alignment = {'L': 0, 'C': 1, 'R': 2}
        pos = alignment[align] if align in alignment else 0
        msg = self.esc.ascii_command('ESC', 'a', pos)
        if self.send(msg):
            print('Justify {} send'.format(align))

    def bold_text(self, n=0):
        # n = 1 BOLD | n = 0 NORMAL
        bold = 1 if n else 0
        msg = self.esc.ascii_command('ESC', 'E', bold)
        if self.send(msg):
            print('Bold send')

    def cut(self, partial=None):
        msg = self.esc.ascii_command('GS', 'V', '0') if not partial else \
            self.esc.ascii_command('GS', 'V', '1')
        # msg = self.esc.dec_command(29, 86, 48)
        if self.send(msg):
            print('Cut send')

    def test(self):
        #self.receive()
        self.justify('C')
        #self.receive()
        self.print('Centro')
        #self.receive()
        self.justify('R')
        #self.receive()
        self.bold_text(1)
        #self.receive()
        self.print('Derecha negra')
        #self.receive()
        self.justify()
        #self.receive()
        self.bold_text(0)
        #self.receive()
        self.print('Izquierda normal')
        #self.receive()
        self.esc.encoding('utf-8')
        self.print('Como no estás experimentado en las cosas del mundo, todas '
                   'las cosas que tienen algo de dificultad te parecen '
                   'imposibles. Confía en el tiempo, que suele dar dulces '
                   'salidas a muchas amargas dificultades.')
        #self.receive()
        #self.line_feed(6)
        #self.receive()
        #msg = self.esc.ascii_command('FF')
        #self.send(msg)
        #self.receive()
        self.cut(partial=True)
        #self.receive()


if __name__ == '__main__':
    port = select_device()
    print('Seleccionado {}'.format(port))
    impresora = Prynter(port=port, printer='epson')
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
