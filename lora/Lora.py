#-*- coding: utf8 -*-

# Docs:
# http://www.hoperf.com/upload/rf/RFM95_96_97_98W.pdf
# http://www.semtech.com/images/datasheet/sx1276.pdf

class Lora:
    def __init__(self, driver, regset):
        self.driver = driver
        self.regset = regset

    def read_reg(self, reg):
        return self.driver.xfer([reg & 0x7f, 0x00])[1]

    def write_reg(self, reg, value):
        self.driver.xfer([reg | 0x80, value])

    def read_version(self):
        return self.read_reg(self.regset.RegVersion)
