import board
import time
import struct
import pew

pew.init()

i2c = board.I2C()
i2c.try_lock()
i2c.writeto(25, b'\x24\x80')
time.sleep(0.01)
i2c.writeto(25, b'\x20\x77')
i2c.writeto(25, b'\x23\x88')

buffer = bytearray(6)
screen = pew.Pix()
while True:
    i2c.writeto(25, b'\xa8', stop=False)
    i2c.readfrom_into(25, buffer)
    x, y, z = struct.unpack('<hhh', buffer)
    a = 2 - x // 2500
    b = z // 2500 + 4
    screen.pixel(a, b, 3)
    pew.show(screen)
    screen.pixel(a, b, 1)
    pew.tick(1/6)
