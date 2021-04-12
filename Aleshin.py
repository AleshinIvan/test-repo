import RPi.GPIO as GPIO
import time

bit_depth = 8
def decToBinList(decNumber):
    a = []
    for i in range(8):
        a.append(decNumber%2)
        decNumber//=2
    return a[::-1]

def num2dac(value):
    value = decToBinList(value)
    for j in range(8):
        GPIO.output(D[j], value[j])
    time.sleep(0.02)

def dac_data(data):
    for i in range(0, bit_depth):
        GPIO.output(D[i], data[i])

def adc_procedure():
    for j in range(0, 2**bit_depth):
        num2dac(j)
        time.sleep(0.0001)
        if GPIO.input(4) == 0:
            print("j =", j, "V =", round(j*3.26/255*100)/100)
            return j

D = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(D+[17], GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.output(17, 1)

# V = 120
"""try:
    while True:
        e = int(input())
        if e < 0:
            1/0
        elif e == -1:
            exit()
        num2dac(e)
        print("V =", round(e*3.26/255*100)/100)
    
except ZeroDivisionError:
    print("0 to 255")
except ValueError:
    print("0 to 255")"""

while True:
    adc_procedure()
       
        