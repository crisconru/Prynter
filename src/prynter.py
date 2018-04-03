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
        super().__init__(port=port)
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
        msg = escpos.esc_command('ESC', '@')
        if self.send(msg):
            print('Initialization send')


if __name__ == '__main__':
    port = select_device()
    print('Seleccionado {}'.format(port))
    impresora = Prynter(port=port)
