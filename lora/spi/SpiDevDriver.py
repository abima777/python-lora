#-*- coding: utf8 -*-

import spidev

class SpiDevDriver:
    def __init__(self, bus=0, device=0, max_speed_hz=4000000):
        self.bus = bus
        self.device = device
        self.max_speed_hz = max_speed_hz
        self.spidev = spidev.SpiDev()

    def open(self):
        self.spidev.open(self.bus, self.device)
        self.spidev.bits_per_word = 8
        self.spidev.cshigh = False
        self.spidev.loop = False
        self.spidev.lsbfirst = False
        self.spidev.max_speed_hz = self.max_speed_hz
        self.spidev.mode = 0b00
        self.spidev.threewire = False

    def close(self):
        self.spidev.close()

    def xfer(self, values):
        return self.spidev.xfer2(values)
