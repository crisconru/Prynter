# Non ASCII characters
esc_hex = {
    'NUL': '00',
    'SOH': '01',
    'STX': '02',
    'ETX': '03',
    'EOT': '04',
    'ENQ': '05',
    'ACK': '06',
    'BEL': '07',
    'BS': '08',
    'TAB': '09',
    'LF': '0A',
    'VT': '0B',
    'FF': '0C',
    'CR': '0D',
    'SO': '0E',
    'SI': '0F',
    'DLE': '10',
    'DC1': '11',
    'DC2': '12',
    'DC3': '13',
    'DC4': '14',
    'NAK': '15',
    'SYN': '16',
    'ETB': '17',
    'CAN': '18',
    'EM': '19',
    'SUB': '1A',
    'ESC': '1B',
    'FS': '1C',
    'GS': '1D',
    'RS': '1E',
    'US': '1F',
    'SP': '20',
    'DEL': '7F'
}

esc_dec = {
    'NUL': 0,
    'SOH': 1,
    'STX': 2,
    'ETX': 3,
    'EOT': 4,
    'ENQ': 5,
    'ACK': 6,
    'BEL': 7,
    'BS': 8,
    'HT': 9,
    'LF': 10,
    'VT': 11,
    'FF': 12,
    'CR': 13,
    'SO': 14,
    'SI': 15,
    'DLE': 16,
    'DC1': 17,
    'DC2': 18,
    'DC3': 19,
    'DC4': 20,
    'NAK': 21,
    'SYN': 22,
    'ETB': 23,
    'CAN': 24,
    'EM': 25,
    'SUB': 26,
    'ESC': 27,
    'FS': 28,
    'GS': 29,
    'RS': 30,
    'US': 31,
    'SP': 32,
    'DEL': 127
}


def esc_command_hex(*args):
    msg = bytearray()
    for i in args:
        aux = None
        if i in esc_hex:
            aux = bytearray.fromhex(esc_hex[i])
        elif isinstance(i, str):
            aux = i.encode('ascii')
        elif isinstance(i, int):
            aux = bytes(chr(i), 'ascii')
        if aux is not None:
            msg.extend(aux)
    return msg


def esc_command_dec(*args):
    msg = bytearray()
    for i in args:
        aux = None
        if i in esc_dec:
            aux = bytes(chr(esc_dec[i]), 'utf-8')
        elif isinstance(i, str):
            aux = i.encode('utf-8')
        elif isinstance(i, int):
            aux = bytes(chr(i), 'utf-8')
        if aux is not None:
            msg.extend(aux)
    return msg


if __name__ == '__main__':
    print('Inicializacion -> ESC @')
    print(esc_command_hex('ESC', '@'))
    print('Mando texto -> Hola mundo')
    print(esc_command_hex('Hola mundo'))
    print('Imprimir linea -> LF')
    print(esc_command_hex('LF'))
