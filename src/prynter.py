import serial
from serial.tools.list_ports import comports

def select_device():
    print('Elegir impresora térmica:')
    i = 0
    for device in comports():
        print('{}) {} {} {}'.format(i, device.device, device.description, 
                                    device.manufacturer))
        i += 1
    return input()

if __name__ == '__main__':
    print('Seleccionado {}'.format(select_device()))
