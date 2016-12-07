#!/usr/bin/env python
#-*- coding: utf8 -*-

import lora
import lora.spi
import spidev

spi = lora.spi.SpiDevDriver()
spi.open()

l = lora.Lora(spi)

print "LoRa chip silicon version: 0x%x" % l.read_version()
