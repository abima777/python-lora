# python-lora

Python interface for certain Semtech SX127x and HopeRF RFM9x chips

Python-lora uses the spidev interface only to access the hardware,
so it should be portable to any board providing SPI access (and having
proper Linux support).

The SPI driver is pluggable, so arbitrary data transfer method can be
implemented and used under the LoRa layer.
