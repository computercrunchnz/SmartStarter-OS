ver = "1.0A5"

from machine import I2C, Pin
import time
from pico_i2c_lcd import I2cLcd
import _thread
import machine
from machine import PWM

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

buz = PWM(Pin(17))
buz.freq(4000)

machine.freq(270000000)

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
ic1 = Pin(18, Pin.OUT)
ic2 = Pin(19, Pin.OUT)
ic3 = Pin(20, Pin.OUT)
ipf = Pin(21, Pin.OUT)
ehn = Pin(22, Pin.OUT)
ec2 = Pin(26, Pin.OUT)
ec3 = Pin(27, Pin.OUT)
epf = Pin(28, Pin.OUT)
led = Pin(25, Pin.OUT)

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
led.value(0)

timeup = 0

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

silo = open("sil", "r")
sil = int(silo.read())
silo.close()

def timecurr():
    tm = rtc.datetime()
    year = tm[0]
    month = tm[1]
    day = tm[2]
    hour = tm[4]
    minute = tm[5]
    second = tm[6]
    lcd.move_to(0,1)
    if hour < 10:
        if minute < 10:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("<= Horn 0", hour, ":0", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("<= Horn 0", hour, ":0", minute, ":", second)
                lcd.putstr(str(timed))
        else:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("<= Horn 0", hour, ":", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("<= Horn 0", hour, ":", minute, ":", second)
                lcd.putstr(str(timed))
    else:
        if minute < 10:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("<= Horn ", hour, ":0", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("<= Horn ", hour, ":0", minute, ":", second)
                lcd.putstr(str(timed))
        else:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("<= Horn ", hour, ":", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("<= Horn ", hour, ":", minute, ":", second)
                lcd.putstr(str(timed))

def timecurrbs5():
    tm = rtc.datetime()
    year = tm[0]
    month = tm[1]
    day = tm[2]
    hour = tm[4]
    minute = tm[5]
    second = tm[6]
    lcd.move_to(0,1)
    if hour < 10:
        if minute < 10:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("05:00   0", hour, ":0", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("05:00   0", hour, ":0", minute, ":", second)
                lcd.putstr(str(timed))
        else:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("05:00   0", hour, ":", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("05:00   0", hour, ":", minute, ":", second)
                lcd.putstr(str(timed))
    else:
        if minute < 10:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("05:00   ", hour, ":0", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("05:00   ", hour, ":0", minute, ":", second)
                lcd.putstr(str(timed))
        else:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("05:00   ", hour, ":", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("05:00   ", hour, ":", minute, ":", second)
                lcd.putstr(str(timed))


def c2():
    global brd
    global bru
    global bld
    global blu
    global e1m
    global e2m
    global e3m
    global e4m
    global e5m
    global ec1
    global i1m
    global i2m
    global i3m
    global i4m
    global i5m
    global buzz
    global ic1
    global ic2
    global ic3
    global ipf
    global ehn
    global ec2
    global ec3
    global epf
    global led
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
    global dns
    global timeup
    global buz
    global sil
    while True:
        time.sleep(0.2)
        while scr == "Start":
            time.sleep(0.2)
            if bru.value() == True:
                scr = "Race"
                if sil == 0:
                    buz.duty_u16(4000)
                time.sleep(1)
                if sil == 0:
                    buz.duty_u16(000)
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
            elif second == 55:
                if sil == 0:
                    buz.duty_u16(4000)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 56:
                if sil == 0:
                    buz.duty_u16(4000)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 57:
                if sil == 0:
                    buz.duty_u16(4000)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 58:
                if sil == 0:
                    buz.duty_u16(4000)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 59:
                if sil == 0:
                    buz.duty_u16(4000)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 00:
                if sil == 0:
                    buz.duty_u16(4000)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            while bld.value() == True:
                if eh == 1:
                    ehn.value(1)
                if sil == 0:
                    buz.duty_u16(4000)
            if eh == 1:
                ehn.value(0)
            if sil == 0:
                buz.duty_u16(000)
        while scr == "Sequence":
            time.sleep(0.2)
            if bru.value() == True:
                scr = "Race"
                buz.duty_u16(4000)
                time.sleep(1)
                buz.duty_u16(000)
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
            elif sl == 5:
                if time.time() == (timeup - 243):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 242):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 241):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 240):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 63):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 62):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 61):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 60):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 3):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 2):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 1):
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == timeup:
                    if sil == 0:
                        buz.duty_u16(4000)
                        time.sleep(0.2)
                        buz.duty_u16(000)
            while bld.value() == True:
                if eh == 1:
                    ehn.value(1)
                if sil == 0:
                    buz.duty_u16(4000)
            if eh == 1:
                ehn.value(0)
            if sil == 0:
                buz.duty_u16(000)

rtc = machine.RTC()

rtc.datetime((2008, 2, 26, 0, 13, 40, 00, 0))

lcd.clear()
lcd.putstr("SmartStarter")
lcd.show_cursor()
lcd.blink_cursor_on()
if sil == 0:
    buz.duty_u16(4000)
time.sleep(1)
if sil == 0:
    buz.duty_u16(0)
lcd.hide_cursor()
lcd.clear()

_thread.start_new_thread(c2, ())

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
            if sil == 0:
                buz.duty_u16(4000)
            if eh == 1:
                ehn.value(1)
        if eh == 1:
            ehn.value(0)
        if sil == 0:
            buz.duty_u16(000)
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
        while bld.value() == True:
            if sil == 0:
                buz.duty_u16(4000)
            if eh == 1:
                ehn.value(1)
        if sil == 0:
            buz.duty_u16(000)
        if eh == 1:
            ehn.value(0)
        if bru.value() == True:
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
        elif second == 56:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 4s")
        elif second == 57:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 3s")
        elif second == 58:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 2s")
        elif second == 59:
            lcd.move_to(0,0)
            lcd.putstr("Starting in 1s")
        elif second == 00:
            scr = "Sequence"
            if sl == 5:
                timeup = (time.time() + 300)
            elif sl == 3:
                timeup = (time.time() + 180)
        if bru.value() == True:
            scr = "Race"
            time.sleep(0.2)
    while scr == "Sequence":
        if f1 == 1:
            if sl == 5:
                if scr == "Sequence":
                    timeup = (time.time() + 300)
                    i1m.value(1)
                    i2m.value(1)
                    i3m.value(1)
                    i4m.value(1)
                    i5m.value(1)
                    ic1.value(1)
                    if el == 1:
                        e1m.value(1)
                        e2m.value(1)
                        e3m.value(1)
                        e4m.value(1)
                        e5m.value(1)
                        ec1.value(1)
                    if eh == 1:
                        ehn.value(1)
                    while time.time() < (timeup - 299):
                        lcd.move_to(0,0)
                        lcd.putstr("5:00 C1 Up     X")
                        timecurr()
                    if eh == 1:
                        ehn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 243):
                        lcd.move_to(0,0)
                        srem = (timeup - 240) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("4:0", srem, " C1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("4:", srem, " C1        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 242):
                        lcd.move_to(0,0)
                        lcd.putstr("4:03 P Up 3s   X")
                        timecurr()
                    while time.time() < (timeup - 241):
                        lcd.move_to(0,0)
                        lcd.putstr("4:02 P Up 2s   X")
                        timecurr()
                    while time.time() < (timeup - 240):
                        lcd.move_to(0,0)
                        lcd.putstr("4:01 P Up 1s   X")
                        timecurr()
                    i5m.value(0)
                    ipf.value(1)
                    if el == 1:
                        e5m.value(0)
                        epf.value(1)
                    if eh == 1:
                        ehn.value(1)
                    while time.time() < (timeup - 239):
                        lcd.move_to(0,0)
                        lcd.putstr("4:00 P Up      X")
                        timecurr()
                    if eh == 1:
                        ehn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 180):
                        lcd.move_to(0,0)
                        srem = (timeup - 180) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("3:0", srem, " C1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("3:", srem, " C1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    i4m.value(0)
                    if el == 1:
                        e4m.value(0)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 C1 P      X")
                        timecurr()
                if scr == "Sequence":
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " C1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " C1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    i3m.value(0)
                    if el == 1:
                        e3m.value(0)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 C1 P      X")
                        timecurr()
                if scr == "Sequence":
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " C1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " C1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 62):
                        lcd.move_to(0,0)
                        lcd.putstr("1:03 P Dn 3s   X")
                        timecurr()
                    while time.time() < (timeup - 61):
                        lcd.move_to(0,0)
                        lcd.putstr("1:02 P Dn 2s   X")
                        timecurr()
                    while time.time() < (timeup - 60):
                        lcd.move_to(0,0)
                        lcd.putstr("1:01 P Dn 1s   X")
                        timecurr()
                    i2m.value(0)
                    ipf.value(0)
                    if el == 1:
                        e2m.value(0)
                        epf.value(0)
                    if eh == 1:
                        ehn.value(1)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if eh == 1:
                        ehn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 C1 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 C1 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 C1 Dn 1s  X")
                        timecurr()
                    i1m.value(0)
                    ic1.value(0)
                    if el == 1:
                        e1m.value(0)
                        ec1.value(0)
                    lcd.move_to(0,0)
                    if eh == 1:
                        ehn.value(1)
                    while time.time() == timeup:
                        lcd.putstr("0:00 C1 Down   X")
                        timecurr()
                    if eh == 1:
                        ehn.value(0)
                    scr = "Race"
        time.sleep(1)
        scr = "Race"
    while scr == "ABD":
        lcd.move_to(0,0)
        lcd.putstr("Abandon")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= N,H     AP =>")
        time.sleep(0.2)
        if bru.value() == True:
            scr = "Race"
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
                rso.write(str(rs))
                rso.close()
            else:
                rso = open("rs1", "w")
                rs = 0
                rso.write(str(rs))
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
            if eh == 0:
                eho = open("eh", "w")
                eh = 1
                eho.write(str(eh))
                eho.close()
            elif eh == 1:
                eho = open("eh", "w")
                eh = 0
                eho.write(str(eh))
                eho.close()
        elif brd.value() == True:
            scr = "Config8"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config8":
        lcd.move_to(0,0)
        if sil == 0:
            lcd.putstr("Silent = No ")
        elif sil == 1:
            lcd.putstr("Silent = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.2)
        if bld.value() == True:
            if sil == 0:
                silo = open("sil", "w")
                sil = 1
                silo.write(str(sil))
                silo.close()
            elif sil == 1:
                silo = open("sil", "w")
                sil = 0
                silo.write(str(sil))
                silo.close()
        elif brd.value() == True:
            scr = "Config9"
        elif bru.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config9":
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
        lcd.putstr("OSVer = " + ver)
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("         Next =>")
        time.sleep(0.2)
        if brd.value() == True:
            scr = "Config1"
        elif bru.value() == True:
            scr = "Home"
