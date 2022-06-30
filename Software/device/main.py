from machine import PWM, Pin
from time import sleep

motor1 = PWM(Pin(15)) #30-65
motor1.freq(50)
motor2 = PWM(Pin(14)) #30-51-65
motor2.freq(50)

def set_motor_position(percent, motorNo):
    oFinal =  int((percent - 1) * (2600000 - 350000) / (100 - 1) + 350000)
    #print(oFinal)
    if motorNo == 1:
        motor1.duty_ns(oFinal)
    elif motorNo == 2:
        motor2.duty_ns(oFinal)
    else:
        print("Error: Unavailable Motor (motor" + str(motorNo) + ")")

def shutdown():
    x=50
    delay=0.02
    for i in range(1,21):
        set_motor_position(x,2)
        x=x+1
        delay = delay + delay*.07
        sleep(delay)
    delay= 0.02
    for i in range(1,41):
        set_motor_position(x,2)
        x=x-1
        delay = delay + delay*.035
        sleep(delay)
    delay= 0.02
    for i in range(1,24):
        set_motor_position(x,2)
        x=x+1
        delay = delay + delay*.07
        sleep(delay)
    delay= 0.02
    sleep(0.2)
    for i in range(1,25):
        set_motor_position(x,1)
        x=x-1
        delay = delay + delay*.07
        sleep(delay)
    set_motor_position(28,1)
    sleep(.2)
    set_motor_position(30,1)
    print("Shutting Down....")
    
def startUp():
    x = 30
    set_motor_position(52,2)
    for i in range(1,28):
        set_motor_position(x, 1)
        x=x+1
        sleep(.05)

def main():
    set_motor_position(50, 1)
              
if __name__ == "__main__":
    main()