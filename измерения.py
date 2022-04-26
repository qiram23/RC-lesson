import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule=17
comparator = 4

def decimal2binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(leds,signal)
    return signal

def adc():
    for value in range(256):
        values.append(value)
        signal=num2dac(value)
        time.sleep(0.007)
        voltage=value / levels * maxVoltage
        comparatorValue=GPIO.input(comparator)
        miis.append(voltage)
        if comparatorValue == 0:
            print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
            measures.append(voltage)
            return value
        

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

signal=0
value=0

measures=[]
miis=[]
values=[]

try:
    GPIO.output(troykaModule,GPIO.HIGH)
    t1=time.time()
    while True:
        for value in range(256):
            print(value)
            values.append(value)
            signal=num2dac(value)
            time.sleep(0.01)
            voltage=value / levels * maxVoltage
            comparatorValue=GPIO.input(comparator)
            if comparatorValue == 0:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                measures.append(voltage)
        if voltage>=3.1:
            GPIO.output(troykaModule,GPIO.LOW)
            break
    
    while True: 
        for value in range(255, -1, -1):
            print(value)
            values.append(value)
            signal=num2dac(value)
            time.sleep(0.01)
            voltage=value / levels * maxVoltage
            comparatorValue=GPIO.input(comparator)
            if comparatorValue == 0:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                measures.append(voltage)
        if value==0:
            t2=time.time()
            break
    t=t2-t1
    print(t)

    measures_str = [str(item) for item in measures]
    with open("data.txt", "w") as f:
        f.write("\n".join(measures_str))
    

finally:
    GPIO.output(leds,GPIO.LOW)
    GPIO.cleanup(leds)
    GPIO.output(troykaModule,GPIO.LOW)
    GPIO.cleanup(troykaModule)
    print("GPIO cleanup completed")