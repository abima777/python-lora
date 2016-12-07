#-*- coding: utf8 -*-

class Lora:
    def __init__(self, driver):
        self.driver = driver

    def read_reg(self, reg):
        return self.driver.xfer([reg & 0x7f, 0x00])[1]

    def write_reg(self, reg, value):
        self.driver.xfer([reg | 0x80, value])

    def read_version(self):
        return self.read_reg(0x42)
