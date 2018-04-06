# Prynter

Modulo Python que implementa el protocolo ESC-POS para poder trabajar con impresoras térmicas

# escpos
Es un conversor al protocolo ESCPOS, todo lo que entra lo pasa a bytes.  
Si mando -> 'ESC', '@'
Lo transforma a -> 27, 64

Problemas
* Si quiero pasar -> 27, 64 => resuelto con esc_command_dec
* Si quiero pasar -> 'ESC', 'd', 6 => necesito que transforme los ESC in commands, los strings en bytes from hex, y los int en bytes