#!/usr/bin/env python
#-*- coding: utf8 -*-

import lora
import lora.spi
import lora.RFM9x_LoRa
import spidev

spi = lora.spi.SpiDevDriver()
spi.open()

l = lora.Lora(driver=spi,regset=lora.RFM9x_LoRa)

print "LoRa chip silicon version: 0x%x" % l.read_version()
