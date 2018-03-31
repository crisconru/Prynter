import serial
from serial.tools.list_ports import comports



def command(*args):
    msg = bytearray()
    for i in args:
        if i in esc:
            msg.append(byesc[args]
        else:


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


if __name__ == '__main__':
    port = select_device()
    print('Seleccionado {}'.format(port))
    impresora = Prynter(port=port)
