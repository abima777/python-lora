# python-lora

Python interface for certain Semtech SX127x and HopeRF RFM9x chips:

* Semtech SX1276
* Semtech SX1277
* Semtech SX1278
* Semtech SX1279
* HopeRF RFM95W
* HopeRF RFM96W
* HopeRF RFM97W
* HopeRF RFM98W

Python-lora uses the spidev interface only to access the hardware,
so it should be portable to any board providing SPI access (and having
proper Linux support).

The SPI driver is pluggable, so arbitrary data transfer method can be
implemented and used under the LoRa layer.
