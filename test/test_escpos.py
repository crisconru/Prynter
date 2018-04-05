from src import escpos


def test_esc_hex():
    esc = b'\x1b'
    assert escpos.esc_command_hex('ESC') == esc


def test_esc_hex_initialization():
    esc = b'\x1b@'
    assert escpos.esc_command_hex('ESC', '@') == esc


def test_esc_hex_text():
    esc = 'Hello world'.encode('utf-8')
    assert escpos.esc_command_hex('Hello world') == esc


def test_esc_dec():
    esc = b'\x1b'
    assert escpos.esc_command_dec('ESC') == esc


def test_esc_dec_initialization():
    esc = b'\x1b@'
    assert escpos.esc_command_dec('ESC', '@') == esc


def test_esc_dec_text():
    esc = 'Hello world'.encode('utf-8')
    assert escpos.esc_command_dec('Hello world') == esc
