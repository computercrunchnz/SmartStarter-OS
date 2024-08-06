#V1A1

from machine import I2C, Pin
import time
from pico_i2c_lcd import I2cLcd
import _thread

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

brd = Pin(2, Pin.IN)
bru = Pin(3, Pin.IN)
bld = Pin(4, Pin.IN)
blu = Pin(5, Pin.IN)
e1m = Pin(6, Pin.OUT)
e2m = Pin(7, Pin.OUT)
e3m = Pin(8, Pin.OUT)
e4m = Pin(9, Pin.OUT)
e5m = Pin(10, Pin.OUT)
ec1 = Pin(11, Pin.OUT)
i1m = Pin(12, Pin.OUT)
i2m = Pin(13, Pin.OUT)
i3m = Pin(14, Pin.OUT)
i4m = Pin(15, Pin.OUT)
i5m = Pin(16, Pin.OUT)
buzz = Pin(17, Pin.OUT)
ic1 = Pin(18, Pin.OUT)
ic2 = Pin(19, Pin.OUT)
ic3 = Pin(20, Pin.OUT)
ipf = Pin(21, Pin.OUT)
ehn = Pin(22, Pin.OUT)
ec2 = Pin(26, Pin.OUT)
ec3 = Pin(27, Pin.OUT)
epf = Pin(28, Pin.OUT)

lte = 0
e1m.value(0)
e2m.value(0)
e3m.value(0)
e4m.value(0)
e5m.value(0)
ec1.value(0)
ec2.value(0)
ec3.value(0)
epf.value(0)
i1m.value(0)
i2m.value(0)
i3m.value(0)
i4m.value(0)
i5m.value(0)
ic1.value(0)
ic2.value(0)
ic3.value(0)
ipf.value(0)

global sta
global scr

sta = 0
scr = "Home"
sl = 5
f1 = 0
f2 = 0
f3 = 0
rs = 0
el = 1
eh = 1
lte = 0

def bz():
    bzt = 0
    while bzt < 50:
        buzz.value(1)
        time.sleep(0.001)
        buzz.value(0)
        time.sleep(0.001)
        bzt = bzt + 1

lcd.clear()
lcd.putstr("SmartStarter")
lcd.show_cursor()
lcd.blink_cursor_on()
bz()
time.sleep(3)
lcd.hide_cursor()
lcd.clear()

while True:
    lcd.clear()
    while scr == "Home":
        lcd.move_to(0,0)
        lcd.putstr("<= Start  ABD =>")
        lcd.move_to(0,1)
        lcd.putstr("<= Horn   CFG =>")
        time.sleep(0.2)
        if blu.value() == True:
            scr = "Start"
        while bld.value() == True:
            bz()
        if brd.value() == True:
            scr = "Config1"
        elif bru.value() == True:
            scr = "ABD"
    lcd.clear()
    while scr == "Start":
        lcd.move_to(0,0)
        lcd.putstr("Starting in 5s")
        lcd.move_to(0,1)
        if sl == 5:
            lcd.putstr("05:00")
        elif sl == 3:
            lcd.putstr("03:00")
        lcd.move_to(15,0)
        lcd.putchar("X")
        bz()
        time.sleep(0.5)
        lcd.move_to(0,0)
        lcd.putstr("Starting in 4s")
        bz()
        time.sleep(0.5)
        lcd.move_to(0,0)
        lcd.putstr("Starting in 3s")
        bz()
        time.sleep(0.5)
        lcd.move_to(0,0)
        lcd.putstr("Starting in 2s")
        bz()
        time.sleep(0.5)
        lcd.move_to(0,0)
        lcd.putstr("Starting in 1s")
        bz()
        bz()
        lcd.move_to(0,0)
        lcd.putstr("Starting")
        scr = "Home"
    lcd.clear()
    while scr == "ABD":
        lcd.move_to(0,0)
        lcd.putstr("Abandon")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= N,H     AP =>")
        time.sleep(0.2)
        if bru.value() == True:
            scr = "Home"
        elif brd.value() == True:
            scr = "AP"
            ehn.value(1)
            time.sleep(1)
            ehn.value(0)
            time.sleep(0.5)
            ehn.value(1)
            time.sleep(1)
            ehn.value(0)
        elif bld.value() == True:
            scr = "NHA"
            ehn.value(1)
            time.sleep(1)
            ehn.value(0)
            time.sleep(0.5)
            ehn.value(1)
            time.sleep(1)
            ehn.value(0)
            time.sleep(0.5)
            ehn.value(1)
            time.sleep(1)
            ehn.value(0)
    lcd.clear()
    while scr == "AP":
        lcd.move_to(0,0)
        lcd.putstr("AP Up")
        lcd.move_to(0,1)
        lcd.putstr("<= Horn  Down =>")
        e1m.value(1)
        e3m.value(1)
        e5m.value(1)
        epf.value(1)
        ec1.value(1)
        i1m.value(1)
        i3m.value(1)
        i5m.value(1)
        ipf.value(1)
        ic1.value(1)
        time.sleep(0.2)
        while bld.value() == 1:
            ehn.value(1)
            bz()
            ehn.value(0)
        if brd.value() == 1:
            scr = "ABD"
            e1m.value(0)
            e3m.value(0)
            e5m.value(0)
            epf.value(0)
            ec1.value(0)
            i1m.value(0)
            i3m.value(0)
            i5m.value(0)
            ipf.value(0)
            ic1.value(0)
    lcd.clear()
    while scr == "NHA":
        lcd.move_to(0,0)
        lcd.putstr("N or H Up")
        lcd.move_to(0,1)
        lcd.putstr("<= Horn  Down =>")
        e1m.value(1)
        e3m.value(1)
        e5m.value(1)
        epf.value(1)
        ec1.value(1)
        ec2.value(1)
        i1m.value(1)
        i3m.value(1)
        i5m.value(1)
        ipf.value(1)
        ic1.value(1)
        ic2.value(1)
        time.sleep(0.2)
        while bld.value() == 1:
            ehn.value(1)
            bz()
            ehn.value(0)
        if brd.value() == 1:
            scr = "ABD"
            e1m.value(0)
            e3m.value(0)
            e5m.value(0)
            epf.value(0)
            ec1.value(0)
            ec2.value(0)
            i1m.value(0)
            i3m.value(0)
            i5m.value(0)
            ipf.value(0)
            ic1.value(0)
            ic2.value(0)
    lcd.clear()
    while scr == "Config1":
        lcd.move_to(0,0)
        if sl == 5:
            lcd.putstr("StartLen = 5m")
        elif sl == 3:
            lcd.putstr("StartLen = 3m")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if sl == 5:
                sl = 3
            elif sl == 3:
                sl = 5
        elif brd.value() == True:
            scr = "Config2"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config2":
        lcd.move_to(0,0)
        if rs == 0:
            lcd.putstr("RollStrt = No ")
        elif rs == 1:
            lcd.putstr("RollStrt = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if rs == 0:
                rs = 1
            elif rs == 1:
                rs = 0
        elif brd.value() == True:
            scr = "Config3"
    lcd.clear()
    while scr == "Config3":
        lcd.move_to(0,0)
        if f1 == 0:
            lcd.putstr("Fleet1 = No ")
        elif f1 == 1:
            lcd.putstr("Fleet1 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if f1 == 0:
                f1 = 1
            elif f1 == 1:
                f1 = 0
        elif brd.value() == True:
            scr = "Config4"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config4":
        lcd.move_to(0,0)
        if f2 == 0:
            lcd.putstr("Fleet2 = No ")
        elif f2 == 1:
            lcd.putstr("Fleet2 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if f2 == 0:
                f2 = 1
            elif f2 == 1:
                f2 = 0
        elif brd.value() == True:
            scr = "Config5"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config5":
        lcd.move_to(0,0)
        if f3 == 0:
            lcd.putstr("Fleet3 = No ")
        elif f3 == 1:
            lcd.putstr("Fleet3 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if f3 == 0:
                f3 = 1
            elif f3 == 1:
                f3 = 0
        elif brd.value() == True:
            scr = "Config6"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config6":
        lcd.move_to(0,0)
        if el == 0:
            lcd.putstr("ExtLight = No ")
        elif el == 1:
            lcd.putstr("ExtLight = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if el == 0:
                el = 1
            elif el == 1:
                el = 0
        elif brd.value() == True:
            scr = "Config7"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config7":
        lcd.move_to(0,0)
        if eh == 0:
            lcd.putstr("ExtHorn = No ")
        elif eh == 1:
            lcd.putstr("ExtHorn = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if eh == 0:
                eh = 1
            elif eh == 1:
                eh = 0
        elif brd.value() == True:
            scr = "Config8"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config8":
        lcd.move_to(0,0)
        if lte == 0:
            lcd.putstr("LTest = No ")
        elif lte == 1:
            lcd.putstr("LTest = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if lte == 0:
                lte = 1
                e1m.value(1)
                e2m.value(1)
                e3m.value(1)
                e4m.value(1)
                e5m.value(1)
                ec1.value(1)
                ec2.value(1)
                ec3.value(1)
                epf.value(1)
                i1m.value(1)
                i2m.value(1)
                i3m.value(1)
                i4m.value(1)
                i5m.value(1)
                ic1.value(1)
                ic2.value(1)
                ic3.value(1)
                ipf.value(1)
            elif lte == 1:
                lte = 0
                e1m.value(0)
                e2m.value(0)
                e3m.value(0)
                e4m.value(0)
                e5m.value(0)
                ec1.value(0)
                ec2.value(0)
                ec3.value(0)
                epf.value(0)
                i1m.value(0)
                i2m.value(0)
                i3m.value(0)
                i4m.value(0)
                i5m.value(0)
                ic1.value(0)
                ic2.value(0)
                ic3.value(0)
                ipf.value(0)
        elif brd.value() == True:
            scr = "Config10"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config10":
        lcd.move_to(0,0)
        lcd.putstr("OSVer = 1A1")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("         Next =>")
        time.sleep(0.2)
        if brd.value() == True:
            scr = "Config1"
        elif bru.value() == True:
            scr = "Home"