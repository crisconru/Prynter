from src import escpos


def test_esc():
    esc = b'\x1b'
    assert escpos.esc_command('ESC') == esc


def test_esc_initialization():
    esc = b'\x1b@'
    assert escpos.esc_command('ESC', '@') == esc


def test_esc_text():
    esc = 'Hello world'.encode('utf-8')
    assert escpos.esc_command('Hello world') == esc
