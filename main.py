from machine import ADC
from time import sleep
adc = ADC (26)

while True:
    
    val = adc.read_u16 ()
    
    V = (val*3.3) / 65535
    
    T = (V*1) / 0.01
    sleep (1)
    
    print ("Temperatura: {:.2f}".format(T))