from machine import I2C, Pin
import time
from pico_i2c_lcd import I2cLcd
import _thread
import machine

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
global sl
global f1
global f2
global f3
global rs
global el
global eh
global lte
global ibz

stao = open("sta", "r")
sta = stao.read(1)
stao.close()

scr = "TimeYN"

slo = open("sl", "r")
sl = int(slo.read())
slo.close()

f1o = open("f1", "r")
f1 = int(f1o.read())
f1o.close()

f2o = open("f2", "r")
f2 = int(f2o.read())
f2o.close()

f3o = open("f3", "r")
f3 = int(f3o.read())
f3o.close()

rso = open("rs1", "r")
rs = int(rso.read())
rso.close()

elo = open("el", "r")
el = int(elo.read())
elo.close()

eho = open("eh", "r")
eh = int(eho.read())
eho.close()

ibzo = open("ibz", "r")
ibz = int(ibzo.read())
ibzo.close()

lteo = open("lte", "r")
lte = int(lteo.read())
lteo.close()

def bz():
    bzt = 0
    #while bzt = 0:#50
        #buzz.value(1)
        #time.sleep(0.001)
        #buzz.value(0)
        #time.sleep(0.001)
        #bzt = bzt + 1
    
rtc = machine.RTC()

rtc.datetime((2008, 2, 26, 0, 13, 40, 00, 0))

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
    while scr == "TimeYN":
        lcd.move_to(0,0)
        lcd.putstr("Set DateTime?")
        lcd.move_to(0,1)
        lcd.putstr("<= No     Yes =>")
        time.sleep(0.2)
        if bld.value() == True:
            scr = "Home"
        elif brd.value() == True:
            scr = "Time1"
            tm = rtc.datetime()
            year = tm[0]
            month = tm[1]
            day = tm[2]
            hour = tm[4]
            minute = tm[5]
            second = tm[6]
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time1":
        lcd.move_to(0,0)
        lcd.putstr("<= Up  Year:" + str(year))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if blu.value() == True:
            year = year + 1
        elif bld.value() == True:
            year = year - 1
        elif brd.value() == True:
            scr = "Time2"
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time2":
        lcd.move_to(0,0)
        if month < 10:
            lcd.putstr("<= Up    Month:" + str(month))
        elif month >= 10:
            lcd.putstr("<= Up   Month:" + str(month))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if blu.value() == True:
            if month <= 12:
                month = month + 1
        elif bld.value() == True:
            if month > 1:
                month = month - 1
        elif brd.value() == True:
            scr = "Time3"
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time3":
        lcd.move_to(0,0)
        if day < 10:
            lcd.putstr("<= Up      Day:" + str(day))
        elif day >= 10:
            lcd.putstr("<= Up     Day:" + str(day))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if blu.value() == True:
            if day < 32:
                day = day + 1
        elif bld.value() == True:
            if day > 0:
                day = day - 1
        elif brd.value() == True:
            scr = "Time4"
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time4":
        lcd.move_to(0,0)
        if hour < 10:
            lcd.putstr("<= Up     Hour:" + str(hour))
        elif hour >= 10:
            lcd.putstr("<= Up    Hour:" + str(hour))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if blu.value() == True:
            if hour < 25:
                hour = hour + 1
        elif bld.value() == True:
            if hour > 1:
                hour = hour - 1
        elif brd.value() == True:
            scr = "Time5"
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time5":
        lcd.move_to(0,0)
        if hour < 10:
            lcd.putstr("<= Up   Minute:" + str(minute))
        elif hour >= 10:
            lcd.putstr("<= Up  Minute:" + str(minute))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if blu.value() == True:
            if minute < 60:
                minute = minute + 1
        elif bld.value() == True:
            if minute > 0:
                minute = minute - 1
        elif brd.value() == True:
            scr = "Time6"
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time6":
        lcd.move_to(0,0)
        if second < 10:
            lcd.putstr("        Second:" + str(second))
        elif second >= 10:
            lcd.putstr("       Second:" + str(second))
        lcd.move_to(0,1)
        lcd.putstr("<= Set0  Exit =>")
        time.sleep(0.2)
        if bld.value() == True:
            second = 0
            rtc.datetime((year, month, day, 0, hour, minute, second, 0))
        elif brd.value() == True:
            scr = "Home"
            rtc.datetime((year, month, day, 0, hour, minute, second, 0))
        if bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Home":
        lcd.move_to(0,0)
        lcd.putstr("<= Race  Time =>")
        lcd.move_to(0,1)
        lcd.putstr("<= Horn   CFG =>")
        time.sleep(0.2)
        if blu.value() == True:
            scr = "Race"
        while bld.value() == True:
            bz()
        if brd.value() == True:
            scr = "Config1"
        elif bru.value() == True:
            scr = "Clock"
    lcd.clear()
    while scr == "Race":
        tm = rtc.datetime()
        year = tm[0]
        month = tm[1]
        day = tm[2]
        hour = tm[4]
        minute = tm[5]
        second = tm[6]
        lcd.move_to(0,0)
        if hour < 10:
            if minute < 10:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= Strt 0", hour, ":0", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= Strt 0", hour, ":0", minute, ":", second)
                    lcd.putstr(str(timed))
            else:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= Strt 0", hour, ":", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= Strt 0", hour, ":", minute, ":", second)
                    lcd.putstr(str(timed))
        else:
            if minute < 10:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= Strt ", hour, ":0", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= Strt ", hour, ":0", minute, ":", second)
                    lcd.putstr(str(timed))
            else:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= Strt ", hour, ":", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= Strt ", hour, ":", minute, ":", second)
                    lcd.putstr(str(timed))
                
        lcd.move_to(0,1)
        lcd.putstr("<= Horn   ABD =>")
        time.sleep(0.2)
        if blu.value() == True:
            scr = "Start"
        elif bld.value() == True:
            bz()
        elif bru.value() == True:
            scr = "Home"
        elif brd.value() == True:
            scr = "ABD"
    lcd.clear()
    while scr == "Clock":
        tm = rtc.datetime()
        year = tm[0]
        month = tm[1]
        day = tm[2]
        hour = tm[4]
        minute = tm[5]
        second = tm[6]
        lcd.move_to(0,0)
        if hour < 10:
            if minute < 10:
                if second < 10:
                    timed = '{}{}{}{}{}{}{}'.format("0", hour, ":0", minute, ":0", second, "       X")
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}{}'.format("0", hour, ":0", minute, ":", second, "       X")
                    lcd.putstr(str(timed))
            else:
                if second < 10:
                    timed = '{}{}{}{}{}{}{}'.format("0", hour, ":", minute, ":0", second, "       X")
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}{}'.format("0", hour, ":", minute, ":", second, "       X")
                    lcd.putstr(str(timed))
        else:
            if minute < 10:
                if second < 10:
                    timed = '{}{}{}{}{}{}{}'.format("", hour, ":0", minute, ":0", second, "       X")
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}{}'.format("", hour, ":0", minute, ":", second, "       X")
                    lcd.putstr(str(timed))
            else:
                if second < 10:
                    timed = '{}{}{}{}{}{}{}'.format("", hour, ":", minute, ":0", second, "       X")
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}{}'.format("", hour, ":", minute, ":", second, "       X")
                    lcd.putstr(str(timed))
        lcd.move_to(0,1)
        if month < 10:
            if day < 10:
                dated = '{}{}{}{}{}{}'.format("0", day, "/0", month, "/", year)
                lcd.putstr(dated)
            else:
                dated = '{}{}{}{}{}{}'.format("", day, "/0", month, "/", year)
                lcd.putstr(dated)
        else:
            if day < 10:
                dated = '{}{}{}{}{}{}'.format("0", day, "/", month, "/", year)
                lcd.putstr(dated)
            else:
                dated = '{}{}{}{}{}{}'.format("", day, "/", month, "/", year)
                lcd.putstr(dated)
        time.sleep(0.1)
        if bru.value() == True:
            scr = "Home"
            time.sleep(0.1)
    while scr == "Start":
        tm = rtc.datetime()
        year = tm[0]
        month = tm[1]
        day = tm[2]
        hour = tm[4]
        minute = tm[5]
        second = tm[6]
        if second < 55:
            lcd.move_to(0,0)
            lcd.putstr("Starting on 00")
        lcd.move_to(0,1)
        if sl == 5:
            lcd.putstr("05:00")
        elif sl == 3:
            lcd.putstr("03:00")
        lcd.move_to(15,0)
        lcd.putchar("X")
        if second == 55:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 5s")
            bz()
        elif second == 56:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 4s")
            bz()
        elif second == 57:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 3s")
            bz()
        elif second == 58:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 2s")
            bz()
        elif second == 59:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 1s")
            bz()
        elif second == 00:
            bz()
            lcd.move_to(0,0)
            lcd.putstr("Starting      ")
            time.sleep(1)
            scr = "Race"
        if bru.value() == True:
            scr = "Race"
            time.sleep(0.2)
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
                slo = open("sl", "w")
                sl = 3
                slo.write(str(sl))
                slo.close()
            elif sl == 3:
                slo = open("sl", "w")
                sl = 5
                slo.write(str(sl))
                slo.close()
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
                rso = open("rs1", "w")
                rs = 1
                rso.write(str(sl))
                rso.close()
            elif rs == 1:
                rso = open("rs1", "w")
                rs = 0
                rso.write(str(sl))
                rso.close()
            else:
                rso = open("rs1", "w")
                rs = 0
                rso.write(str(sl))
                rso.close()
        elif brd.value() == True:
            scr = "Config3"
        elif bru.value() == True:
            scr = "Home"
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
                f1o = open("f1", "w")
                f1 = 1
                f1o.write(str(f1))
                f1o.close()
            elif f1 == 1:
                f1o = open("f1", "w")
                f1 = 0
                f1o.write(str(f1))
                f1o.close()
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
                f2o = open("f2", "w")
                f2 = 1
                f2o.write(str(f2))
                f2o.close()
            elif f2 == 1:
                f2o = open("f2", "w")
                f2 = 0
                f2o.write(str(f2))
                f2o.close()
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
                f3o = open("f3", "w")
                f3 = 1
                f3o.write(str(f3))
                f3o.close()
            elif f3 == 1:
                f3o = open("f3", "w")
                f3 = 0
                f3o.write(str(f3))
                f3o.close()
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
                elo = open("el", "w")
                el = 1
                elo.write(str(el))
                elo.close()
            elif el == 1:
                elo = open("el", "w")
                el = 0
                elo.write(str(el))
                elo.close()
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
            if el == 0:
                elo = open("eh", "w")
                el = 1
                elo.write(str(el))
                elo.close()
            elif el == 1:
                elo = open("eh", "w")
                el = 0
                elo.write(str(el))
                elo.close()
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
            scr = "Config9"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config9":
        lcd.move_to(0,0)
        lcd.putstr("OSVer = 1A2")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("         Next =>")
        time.sleep(0.2)
        if brd.value() == True:
            scr = "Config1"
        elif bru.value() == True:
            scr = "Home"