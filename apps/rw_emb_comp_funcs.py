import os
from fcntl import ioctl

RD_SWITCHES = 24929
RD_PBUTTONS = 24930
WR_L_DISPLAY = 24931
WR_R_DISPLAY = 24932
WR_RED_LEDS = 24933
WR_GREEN_LEDS = 24934

SEVEN_SEGMENT_OPTIONS = {
    0: 0b01000000,
    1: 0b01111001, 
    2: 0b00100100,
    3: 0b00110000,
    4: 0b00011001,
    5: 0b00010010,
    6: 0b00000010,
    7: 0b01111000,
    8: 0b00000000,
    9: 0b00010000,
    "OFF": 0b11111111
}

class RWEmbCompFuncs:
    def __init__(self):
        self.fd = os.open('/dev/mydev', os.O_RDWR)
        self.buttons = {
            '0b111': "A", # 7
            '0b1001': "B", # 9
            '0b1010': "C", # 10
            '0b1011': "D", # 11
            '0b1100': "E" # 12
            '0b1101': "F", # 13
            '0b1110': "G", # 14
            '0b1111': "H", # 15
        }

    def __del__(self):
        os.close(self.fd)

    def seven_segment_encoder(self, num):
        display = 0
        num_digits = 0

        while True:
            digit = num % 10
            display |= (SEVEN_SEGMENT_OPTIONS[digit] << 8 * num_digits)
            num_digits += 1
            num = num // 10
            
            if num == 0:
                break

        for i in range (num_digits, num_digits + (4 - num_digits)):
            display |= (SEVEN_SEGMENT_OPTIONS["OFF"] << 8 * i)

        return display

    def seven_segment(self, num, display):
        data = seven_segment_encoder(num)
        
        ioctl(self.fd, display)
        retval = os.write(self.fd, data.to_bytes(4, 'little'))

    def red_leds(self, j):
        data = 0b111111111111111111

        for i in range(0, j):
            data >>= 1
        
        ioctl(self.fd, WR_RED_LEDS)
        os.write(self.fd, data.to_bytes(4,'little'))

    def green_leds(self, j):
        data = 0b11111111

        for i in range(0, j):
            data >>= 1
        
        ioctl(self.fd, WR_GREEN_LEDS)
        os.write(self.fd, data.to_bytes(4,'little'))

    def read_button(self):
        ioctl(self.fd, RD_PBUTTONS)
        button = os.read(self.fd, 4)
        button = bin(int.from_bytes(button, 'little'))

        return button

    def read_switches(self):
        ioctl(self.fd, RD_SWITCHES)
        switches = os.read(self.fd, 4)
        switches = bin(int.from_bytes(switches, 'little'))  

        return switches