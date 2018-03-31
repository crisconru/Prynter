# Non ASCII characters
esc = {
    'NUL': '00', 'SOH': '01', 'STX': '02', 'ETX': '03', 'EOT': '04',
    'ENQ': '05', 'ACK': '06', 'BEL': '07', 'BS': '08', 'TAB': '09', 'LF': '0A',
    'VT': '0B', 'FF': '0C', 'CR': '0D', 'SO': '0E', 'SI': '0F', 'DLE': '10',
    'DC1': '11', 'DC2': '12', 'DC3': '13', 'DC4': '14', 'NAK': '15',
    'SYN': '16', 'ETB': '17', 'CAN': '18', 'EM': '19', 'SUB': '1A',
    'ESC': '1B', 'FS': '1C', 'GS': '1D', 'RS': '1E', 'US': '1F', 'SP': '20',
    'DEL': '7F'
}


def esc_command(*args):
    command = bytearray()
    for i in args:
        aux = None
        if i in esc:
            aux = bytearray.fromhex(esc[i])[0]
        elif isinstance(i, str):
            aux = i.encode
        elif isinstance(i, int):
            aux = bytes([i])
        command.extend(aux)
    print(command)

