import os
import time as t

active = False
try:
    from fcntl import ioctl
    active = True
except ImportError:
    print("This module is not supported on this platform")

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

def check_active(func):
    def wrapper(self, *args, **kwargs):
        if not self.active:
            print("The device is not active.")
            return
        return func(self, *args, **kwargs)
    return wrapper

class RWEmbCompFuncs:
    def __init__(self):
        self.active = active
        self.buttons = {
            '0b111': "A", # 7
            '0b1001': "B", # 9
            '0b1010': "C", # 10
            '0b1011': "D", # 11
            '0b1100': "E", # 12
            '0b1101': "F", # 13
            '0b1110': "G", # 14
            '0b1111': "H" # 15
        }
        try:
            self.fd = os.open('/dev/mydev', os.O_RDWR)
        except:
            self.active = False
            print("Could not open /dev/mydev")

    def __del__(self):
        os.close(self.fd)

    def _seven_segment_encoder(self, num):
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

    def _number_to_binary(self, number):
        ans = 0
        for i in range(0, number):
            ans |= (1 << i)
        return ans 

    @check_active
    def seven_segment_r(self, num):
        data = self._seven_segment_encoder(num)
        
        for i in range(0, 2):
            ioctl(self.fd, WR_R_DISPLAY)
            retval = os.write(self.fd, data.to_bytes(4, 'little'))
            t.sleep(0.1)

    @check_active
    def seven_segment_l(self, num):
        data = self._seven_segment_encoder(num)
        
        for i in range(0, 2):
            ioctl(self.fd, WR_L_DISPLAY)
            retval = os.write(self.fd, data.to_bytes(4, 'little'))
            t.sleep(0.1)

    @check_active
    def red_leds(self, number):
        data = self._number_to_binary(number)
        for i in range(0, 2):
            ioctl(self.fd, WR_RED_LEDS)
            os.write(self.fd, data.to_bytes(4,'little'))
            t.sleep(0.1)
        

    @check_active
    def green_leds(self, number):
        data = self._number_to_binary(number)
        for i in range(0, 2):
            ioctl(self.fd, WR_GREEN_LEDS)
            os.write(self.fd, data.to_bytes(4,'little'))
            t.sleep(0.1)

    @check_active
    def read_button(self):
        ioctl(self.fd, RD_PBUTTONS)
        button = os.read(self.fd, 4)
        button = bin(int.from_bytes(button, 'little'))

        return button

    @check_active
    def read_switches(self):
        ioctl(self.fd, RD_SWITCHES)
        switches = os.read(self.fd, 4)
        switches = bin(int.from_bytes(switches, 'little'))  

        return switches