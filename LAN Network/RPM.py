import time
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000


def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    print(f"Raw ADC: {adc}")
    data = ((adc[1] & 3) << 8) + adc[2]
    return data
 
sensor_channel = 1


def main():

    try:
        while True:
           value = read_channel(sensor_channel)
           print(f"Analog: {value}")
           time.sleep(1)
    except KeyboardInterrupt:
        print(f"analog: {value}")
    


if __name__ == "__main__":
    main()
