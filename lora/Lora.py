#-*- coding: utf8 -*-

# Docs:
# http://www.hoperf.com/upload/rf/RFM95_96_97_98W.pdf
# http://www.semtech.com/images/datasheet/sx1276.pdf

class Lora:
    RegFifo = 0x00 # FIFO read/write access
    RegOpMode = 0x01 # Operating mode &  LoRa TM / FSK selection
    RegBitrateMsb = 0x02 # Bit Rate setting, Most Significant Bits
    RegBitrateLsb = 0x03 # Bit Rate setting, Least Significant Bits
    RegFdevMsb = 0x04 # Frequency Deviation setting, Most Significant Bits
    RegFdevLsb = 0x05 # Frequency Deviation setting, Least Significant Bits
    RegFrfMsb = 0x06 # RF Carrier Frequency, Most Significant Bits
    RegFrfMid = 0x07 # RF Carrier Frequency, Intermediate Bits
    RegFrfLsb = 0x08 # RF Carrier Frequency, Least Significant Bits
    RegPaConfig = 0x09 # PA selection and Output Power control
    RegPaRamp = 0x0A # Control of PA ramp time, low phase noise PLL
    RegOcp = 0x0B # Over Current Protection control
    RegLna = 0x0C # LNA settings
    RegRxConfig = 0x0D # (FSK/OOK) AFC, AGC, ctrl
    RegFifoAddrPtr = 0x0D # (LoRa) FIFO SPI pointer
    RegRssiConfig = 0x0E # (FSK/OOK) RSSI
    RegFifoTxBaseAddr = 0x0E # (LoRa) Start Tx data
    RegRssiCollision = 0x0F # (FSK/OOK) RSSI Collision detector
    RegFifoRxBaseAddr = 0x0F # (LoRa) Start Rx data
    RegRssiThresh = 0x10 # RSSI Threshold control
    RegIrqFlags = 0x10 # LoRa state flags
    RegRssiValue = 0x11 # RSSI value in dBm
    RegIrqFlagsMask = 0x11 # Optional flag mask
    RegRxBw = 0x12 # Channel Filter BW Control
    RegFreqIfMsb = 0x12 # IF Frequency - MSB
    RegAfcBw = 0x13 # AFC Channel Filter BW
    RegFreqIFLsb = 0x13 # IF Frequency - LSB
    RegOokPeak = 0x14 # OOK demodulator
    RegSymbTimeoutMsb = 0x14 # Receiver timeout value - MSB
    RegOokFix = 0x15 # Threshold of the OOK demod
    RegSymbTimeoutLsb = 0x15 # Receiver timeout value - LSB
    RegOokAvg = 0x16 # Average of the OOK demod
    RegTxCfg = 0x16 # LoRa transmit parameters
    RegPayloadLength = 0x17 # LoRa Payload length
    RegPreambleMsb = 0x18 # Size of preamble - MSB
    RegPreambleLsb = 0x19 # Size of preamble - LSB
    RegAfcFei = 0x1A # AFC and FEI control
    RegModulationCfg = 0x1A # Modem PHY config
    RegAfcMsb = 0x1B # Frequency correction value of the AFC
    RegRfMode = 0x1B # Test register
    RegAfcLsb = 0x1C # Frequency correction value of the AFC
    RegHopPeriod = 0x1C # FHSS Hop period
    RegFeiMsb = 0x1D
    RegNbRxBytes = 0x1D # Number of received bytes
    RegFeiLsb = 0x1E
    RegRxHeaderInfo = 0x1E # Value of the calculated frequency error Info from last header
    RegPreambleDetect = 0x1F # Settings of the Preamble Detector
    RegRxHeaderCntValue = 0x1F # Number of valid headers received
    RegRxTimeout1 = 0x20 # Timeout Rx request and RSSI
    RegRxPacketCntValue = 0x20 # Number of valid packets received
    RegRxTimeout2 = 0x21 # Timeout RSSI and PayloadReady
    RegModemStat = 0x21 # Live LoRa modem status
    RegRxTimeout3 = 0x22 # Timeout RSSI and  SyncAddress
    RegPktSnrValue = 0x22 # Estimation of last packet SNR
    RegRxDelay = 0x23 # Delay between Rx cycles
    RegRssiValue = 0x23 # Current RSSI
    RegOsc = 0x24 # RC Oscillators Settings, CLKOUT frequency
    RegPktRssiValue = 0x24 # RSSi of last packet
    RegPreambleMsb = 0x25 # Preamble length, MSB
    RegHopChannel = 0x25 # FHSS start channel
    RegPreambleLsb = 0x26 # Preamble length, LSB
    RegRxDataAddr = 0x26 # LoRa rx data pointer
    RegSyncConfig = 0x27 # Sync Word Recognition control
    RegSyncValue1 = 0x28 # Sync word byte 1
    RegSyncValue2 = 0x29 # Sync word byte 2
    RegSyncValue3 = 0x2A # Sync word byte 3
    RegSyncValue4 = 0x2B # Sync word byte 4
    RegSyncValue5 = 0x2C # Sync word byte 5
    RegSyncValue6 = 0x2D # Sync word byte 6
    RegSyncValue7 = 0x2E # Sync word byte 7
    RegSyncValue8 = 0x2F # Sync word byte 8
    RegPacketConfig1 = 0x30 # Packet mode settings
    RegPacketConfig2 = 0x31 # Packet mode settings
    RegPayloadLength = 0x32 # Payload length setting
    RegNodeAdrs = 0x33 # Node address
    RegBroadcastAdrs = 0x34 # Broadcast address
    RegFifoThresh = 0x35 # Fifo threshold, Tx start condition
    RegSeqConfig1 = 0x36 # Top level Sequencer settings
    RegSeqConfig2 = 0x37 # Top level Sequencer settings
    RegTimerResol = 0x38 # Timer 1 and 2 resolution control
    RegTimer1Coef = 0x39 # Timer 1 setting
    RegTimer2Coef = 0x3A # Timer 2 setting
    RegImageCal = 0x3B # Image calibration engine control
    RegTemp = 0x3C # Temperature Sensor value
    RegLowBat = 0x3D # Low Battery Indicator Settings
    RegIrqFlags1 = 0x3E # Status register: PLL Lock state, Timeout, RSSI
    RegIrqFlags2 = 0x3F # Status register: FIFO handling  flags, Low Battery
    RegDioMapping1 = 0x40 # Mapping of pins DIO0 to DIO3
    RegDioMapping2 = 0x41 # Mapping of pins DIO4 and DIO5, ClkOut frequency
    RegVersion = 0x42 # Hope RF ID relating the silicon revision
    RegPllHop = 0x44 # Control the fast frequency hopping mode
    RegTcxo = 0x4B # TCXO or XTAL input setting

    def __init__(self, driver):
        self.driver = driver

    def read_reg(self, reg):
        return self.driver.xfer([reg & 0x7f, 0x00])[1]

    def write_reg(self, reg, value):
        self.driver.xfer([reg | 0x80, value])

    def read_version(self):
        return self.read_reg(Lora.RegVersion)
