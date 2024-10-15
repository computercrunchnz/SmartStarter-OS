ver = "1.0B5"

from machine import I2C, Pin
import time
from pico_i2c_lcd import I2cLcd
import _thread
import machine
from machine import PWM

#Overclock CPU

machine.freq(270000000)

#Display Setup

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

#Buzzer PWM Setup

buz = PWM(Pin(17))
buz.freq(3500)

#IO Setup

lowrightbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
uprightbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)
lowleftbutton = Pin(4, Pin.IN, Pin.PULL_DOWN)
upleftbutton = Pin(5, Pin.IN, Pin.PULL_DOWN)
hornbutton = Pin(28, Pin.IN, Pin.PULL_DOWN)
oneminutelight = Pin(6, Pin.OUT)
twominutelight = Pin(7, Pin.OUT)
threeminutelight = Pin(8, Pin.OUT)
fourminutelight = Pin(9, Pin.OUT)
fiveminutelight = Pin(10, Pin.OUT)
fleetonelight = Pin(11, Pin.OUT)
fleettwolight = Pin(12, Pin.OUT)
fleetthreelight = Pin(13, Pin.OUT)
plight = Pin(14, Pin.OUT)
horn = Pin(22, Pin.OUT)
led = Pin(25, Pin.OUT)


#All Outputs Off

oneminutelight.value(0)
twominutelight.value(0)
threeminutelight.value(0)
fourminutelight.value(0)
fiveminutelight.value(0)
fleetonelight.value(0)
fleettwolight.value(0)
fleetthreelight.value(0)
plight.value(0)
led.value(0)

timeup = 0

start = 0

dispon = 1

#Set Screen

scr = "TimeYN"

#Open saved variables

startlengthopen = open("startlength", "r")
startlength = int(startlengthopen.read())
startlengthopen.close()

fleetoneopen = open("fleetone", "r")
fleetone = int(fleetoneopen.read())
fleetoneopen.close()

fleettwoopen = open("fleettwo", "r")
fleettwo = int(fleettwoopen.read())
fleettwoopen.close()

fleetthreeopen = open("fleetthree", "r")
fleetthree = int(fleetthreeopen.read())
fleetthreeopen.close()

rollingstartopen = open("rollingstart1", "r")
rollingstart = int(rollingstartopen.read())
rollingstartopen.close()

externallightsopen = open("externallights", "r")
externallights = int(externallightsopen.read())
externallightsopen.close()

externalhornopen = open("externalhorn", "r")
externalhorn = int(externalhornopen.read())
externalhornopen.close()

internalbuzzeropen = open("internalbuzzer", "r")
internalbuzzer = int(internalbuzzeropen.read())
internalbuzzeropen.close()

lighttestopen = open("lighttest", "r")
lighttest = int(lighttestopen.read())
lighttestopen.close()

silententopen = open("silent", "r")
silent = int(silententopen.read())
silententopen.close()

waitbeforestartopen = open("waitbeforestart", "r")
waitbeforestart = int(waitbeforestartopen.read())
waitbeforestartopen.close()

#Set Get Time Functions

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
                timed = '{}{}{}{}{}{}'.format("        0", hour, ":0", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("        0", hour, ":0", minute, ":", second)
                lcd.putstr(str(timed))
        else:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("        0", hour, ":", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("        0", hour, ":", minute, ":", second)
                lcd.putstr(str(timed))
    else:
        if minute < 10:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("        ", hour, ":0", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("        ", hour, ":0", minute, ":", second)
                lcd.putstr(str(timed))
        else:
            if second < 10:
                timed = '{}{}{}{}{}{}'.format("        ", hour, ":", minute, ":0", second)
                lcd.putstr(str(timed))
            else:
                timed = '{}{}{}{}{}{}'.format("        ", hour, ":", minute, ":", second)
                lcd.putstr(str(timed))
                
#Set second thread function

def thread2():
    global lowrightbutton
    global uprightbutton
    global lowleftbutton
    global upleftbutton
    global oneminutelight
    global twominutelight
    global threeminutelight
    global fourminutelight
    global fiveminutelight
    global fleetonelight
    global buzz
    global horn
    global fleettwolight
    global fleetthreelight
    global plight
    global led
    global start
    global scr
    global startlength
    global fleetone
    global fleettwo
    global fleetthree
    global rollingstart
    global externallights
    global externalhorn
    global lighttest
    global internalbuzzer
    global dns
    global timeup
    global buz
    global silent
    while True:
        time.sleep(0.2)
        while scr == "Start":
            if uprightbutton.value() == True:
                scr = "Race"
                if silent == 0:
                    buz.duty_u16(3500)
                time.sleep(1)
                if silent == 0:
                    buz.duty_u16(000)
                oneminutelight.value(0)
                twominutelight.value(0)
                threeminutelight.value(0)
                fourminutelight.value(0)
                fiveminutelight.value(0)
                fleetonelight.value(0)
                fleettwolight.value(0)
                fleetthreelight.value(0)
                plight.value(0)
            elif second == 55:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
                    time.sleep(0.2)
            elif second == 56:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
                    time.sleep(0.2)
            elif second == 57:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
                    time.sleep(0.2)
            elif second == 58:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
                    time.sleep(0.2)
            elif second == 59:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
                    time.sleep(0.2)
            elif second == 00:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
                    time.sleep(0.2)
            if silent == 0:
                buz.duty_u16(000)
            while hornbutton.value() == True:
                if externalhorn == 1:
                    horn.value(1)
                    time.sleep(0.2)
                if hornbutton.value() == False:
                    horn.value(0)
                    time.sleep(0.2)
        while scr == "Sequence":
            if uprightbutton.value() == True:
                scr = "Race"
                if silent == 0:
                    buz.duty_u16(3500)
                time.sleep(1)
                if silent == 0:
                    buz.duty_u16(000)
                oneminutelight.value(0)
                twominutelight.value(0)
                threeminutelight.value(0)
                fourminutelight.value(0)
                fiveminutelight.value(0)
                fleetonelight.value(0)
                fleettwolight.value(0)
                fleetthreelight.value(0)
                plight.value(0)
            elif startlength == 5:
                if time.time() == (timeup - 245):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 244):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 243):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 242):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 241):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 240):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 65):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 64):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 63):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 62):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 61):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 60):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 5):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 4):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 3):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 2):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 1):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == timeup:
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                while hornbutton.value() == True:
                    if externalhorn == 1:
                        horn.value(1)
                        time.sleep(0.2)
                    if hornbutton.value() == False:
                        horn.value(0)
                        time.sleep(0.2)
            elif startlength == 3:
                if time.time() == (timeup - 125):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 124):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 123):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 122):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 121):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 120):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 65):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 64):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 63):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 62):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 61):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 60):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 5):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 4):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 3):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 2):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == (timeup - 1):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                elif time.time() == timeup:
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                        time.sleep(0.2)
                while hornbutton.value() == True:
                    if externalhorn == 1:
                        horn.value(1)
                        time.sleep(0.2)
                    if hornbutton.value() == False:
                        horn.value(0)
                        time.sleep(0.2)
        else:
            while hornbutton.value() == True:
                if externalhorn == 1:
                    horn.value(1)
                    time.sleep(0.2)
                if hornbutton.value() == False:
                    horn.value(0)
                    time.sleep(0.2)

rtc = machine.RTC()

rtc.datetime((2008, 2, 26, 0, 13, 40, 00, 0))

#Splash Screen

lcd.clear()
lcd.putstr("SmartStarter")
lcd.show_cursor()
lcd.blink_cursor_on()
if silent == 0:
    buz.duty_u16(3500)
time.sleep(1)
if silent == 0:
    buz.duty_u16(0)
lcd.hide_cursor()
lcd.clear()

#Start Second Thread

_thread.start_new_thread(thread2, ())

#Main Loop

while True:
    lcd.clear()
    while scr == "TimeYN":
        #Set Time Yes or No
        lcd.move_to(0,0)
        lcd.putstr("Set DateTime?")
        lcd.move_to(0,1)
        lcd.putstr("<= No     Yes =>")
        if lowleftbutton.value() == True:
            scr = "Home"
            time.sleep(0.2)
        elif lowrightbutton.value() == True:
            scr = "Time1"
            time.sleep(0.2)
            tm = rtc.datetime()
            year = tm[0]
            month = tm[1]
            day = tm[2]
            hour = tm[4]
            minute = tm[5]
            second = tm[6]
        if uprightbutton.value() == True:
            scr = "Home"
            time.sleep(0.2)
    lcd.clear()
    while scr == "Time1":
        #Set Year
        lcd.move_to(0,0)
        lcd.putstr("<= Up  Year:" + str(year))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if upleftbutton.value() == True:
            year = year + 1
        elif lowleftbutton.value() == True:
            year = year - 1
        elif lowrightbutton.value() == True:
            scr = "Time2"
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time2":
        #Set Month
        lcd.move_to(0,0)
        if month < 10:
            lcd.putstr("<= Up    Month:" + str(month))
        elif month >= 10:
            lcd.putstr("<= Up   Month:" + str(month))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if upleftbutton.value() == True:
            if month <= 12:
                month = month + 1
        elif lowleftbutton.value() == True:
            if month > 1:
                month = month - 1
        elif lowrightbutton.value() == True:
            scr = "Time3"
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time3":
        #Set Day
        lcd.move_to(0,0)
        if day < 10:
            lcd.putstr("<= Up      Day:" + str(day))
        elif day >= 10:
            lcd.putstr("<= Up     Day:" + str(day))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if upleftbutton.value() == True:
            if day < 32:
                day = day + 1
        elif lowleftbutton.value() == True:
            if day > 0:
                day = day - 1
        elif lowrightbutton.value() == True:
            scr = "Time4"
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time4":
        #Set Hour
        lcd.move_to(0,0)
        if hour < 10:
            lcd.putstr("<= Up     Hour:" + str(hour))
        elif hour >= 10:
            lcd.putstr("<= Up    Hour:" + str(hour))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if upleftbutton.value() == True:
            if hour < 25:
                hour = hour + 1
        elif lowleftbutton.value() == True:
            if hour > 1:
                hour = hour - 1
        elif lowrightbutton.value() == True:
            scr = "Time5"
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time5":
        #Set Minute
        lcd.move_to(0,0)
        if hour < 10:
            lcd.putstr("<= Up   Minute:" + str(minute))
        elif hour >= 10:
            lcd.putstr("<= Up  Minute:" + str(minute))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.2)
        if upleftbutton.value() == True:
            if minute < 60:
                minute = minute + 1
        elif lowleftbutton.value() == True:
            if minute > 0:
                minute = minute - 1
        elif lowrightbutton.value() == True:
            scr = "Time6"
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time6":
        #Set Second to 0
        lcd.move_to(0,0)
        if second < 10:
            lcd.putstr("        Second:" + str(second))
        elif second >= 10:
            lcd.putstr("       Second:" + str(second))
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Exit =>")
        time.sleep(0.2)
        if lowleftbutton.value() == True:
            second = 0
            rtc.datetime((year, month, day, 0, hour, minute, second, 0))
        elif lowrightbutton.value() == True:
            scr = "Home"
            rtc.datetime((year, month, day, 0, hour, minute, second, 0))
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Home":
        #Home Screen
        lcd.move_to(0,0)
        lcd.putstr("<= Race  Time =>")
        lcd.move_to(0,1)
        lcd.putstr("<= D.O    CFG =>")
        if upleftbutton.value() == True:
            time.sleep(0.2)
            scr = "Race"
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if dispon == 1:
                lcd.backlight_off()
                dispon = 0
            elif dispon == 0:
                lcd.backlight_on()
                dispon = 1
        if lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config1"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Clock"
    lcd.clear()
    while scr == "Race":
        #Race Menu
        tm = rtc.datetime()
        year = tm[0]
        month = tm[1]
        day = tm[2]
        hour = tm[4]
        minute = tm[5]
        second = tm[6]
        lcd.move_to(0,0)
        lcd.putstr("<= Start       X")
        lcd.move_to(0,1)
        if hour < 10:
            if minute < 10:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  0", hour, ":0", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  0", hour, ":0", minute, ":", second)
                    lcd.putstr(str(timed))
            else:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  0", hour, ":", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  0", hour, ":", minute, ":", second)
                    lcd.putstr(str(timed))
        else:
            if minute < 10:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  ", hour, ":0", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  ", hour, ":0", minute, ":", second)
                    lcd.putstr(str(timed))
            else:
                if second < 10:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  ", hour, ":", minute, ":0", second)
                    lcd.putstr(str(timed))
                else:
                    timed = '{}{}{}{}{}{}'.format("<= ABD  ", hour, ":", minute, ":", second)
                    lcd.putstr(str(timed))
        #Start Sequence
        if upleftbutton.value() == True:
            time.sleep(0.2)
            scr = "Start"
        #Go to Home Menu
        if uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
        #Go to Abandon Menu
        elif lowleftbutton.value() == True:
            time.sleep(0.2)
            scr = "ABD"
    lcd.clear()
    while scr == "Clock":
        #Clock Screen
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
        if uprightbutton.value() == True:
            scr = "Home"
            time.sleep(0.2)
    while scr == "Start":
        #Screen before actual start sequence with countdown to sequence.
        #Check for valid start type
        if fleetone == 1:
            start = 1
        elif fleettwo == 1:
            start = 1
        elif fleetthree == 1:
            start = 1
        else:
            start = 0
        #If valid:
        if start == 1:
           #Get Time
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
            #Turn time into string
            if startlength == 5:
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
            elif startlength == 3:
                if hour < 10:
                    if minute < 10:
                        if second < 10:
                            timed = '{}{}{}{}{}{}'.format("03:00   0", hour, ":0", minute, ":0", second)
                            lcd.putstr(str(timed))
                        else:
                            timed = '{}{}{}{}{}{}'.format("03:00   0", hour, ":0", minute, ":", second)
                            lcd.putstr(str(timed))
                    else:
                        if second < 10:
                            timed = '{}{}{}{}{}{}'.format("03:00   0", hour, ":", minute, ":0", second)
                            lcd.putstr(str(timed))
                        else:
                            timed = '{}{}{}{}{}{}'.format("03:00   0", hour, ":", minute, ":", second)
                            lcd.putstr(str(timed))
                else:
                    if minute < 10:
                        if second < 10:
                            timed = '{}{}{}{}{}{}'.format("03:00   ", hour, ":0", minute, ":0", second)
                            lcd.putstr(str(timed))
                        else:
                            timed = '{}{}{}{}{}{}'.format("03:00   ", hour, ":0", minute, ":", second)
                            lcd.putstr(str(timed))
                    else:
                        if second < 10:
                            timed = '{}{}{}{}{}{}'.format("03:00   ", hour, ":", minute, ":0", second)
                            lcd.putstr(str(timed))
                        else:
                            timed = '{}{}{}{}{}{}'.format("03:00   ", hour, ":", minute, ":", second)
                            lcd.putstr(str(timed))
            lcd.move_to(15,0)
            lcd.putchar("X")
            #Countdown
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
                #Go to actual sequence
                scr = "Sequence"
            #Stop start
            if uprightbutton.value() == True:
                scr = "Race"
                time.sleep(0.2)
        #If invalid
        else:
            lcd.move_to(0,0)
            lcd.putstr("Error! Must have")
            lcd.move_to(0,1)
            lcd.putstr("fleet! Chk conf.")
            time.sleep(2)
            scr = "Race"
    while scr == "Sequence":
        #Sequence
        #Fleet 1
        if fleetone == 1:
            #5 Minute Sequence
            if startlength == 5:
                #Check if sequence hasn't been cancelled
                if scr == "Sequence":
                    timeup = (time.time() + 300)
                    #Operate Horn and Lights
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fourminutelight.value(1)
                        fiveminutelight.value(1)
                        fleetonelight.value(1)
                    while time.time() < (timeup - 299):
                        lcd.move_to(0,0)
                        lcd.putstr("5:00 F1 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 245):
                        #Countdown to 4 Minutes
                        lcd.move_to(0,0)
                        srem = (timeup - 240) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("4:0", srem, " F1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("4:", srem, " F1        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    #Alert User of Light/Flag Change
                    while time.time() < (timeup - 244):
                        lcd.move_to(0,0)
                        lcd.putstr("4:05 P Up 5s   X")
                        timecurr()
                    while time.time() < (timeup - 243):
                        lcd.move_to(0,0)
                        lcd.putstr("4:04 P Up 4s   X")
                        timecurr()
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
                    if externallights == 1:
                        fiveminutelight.value(0)
                        plight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 239):
                        lcd.move_to(0,0)
                        lcd.putstr("4:00 P Up      X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 3 minutes
                    while time.time() < (timeup - 180):
                        lcd.move_to(0,0)
                        srem = (timeup - 180) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("3:0", srem, " F1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("3:", srem, " F1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        fourminutelight.value(0)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 F1 P      X")
                        timecurr()
                if scr == "Sequence":
                    #Countdown to 2 minutes
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " F1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " F1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        threeminutelight.value(0)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 F1 P      X")
                        timecurr()
                if scr == "Sequence":
                    #Countdown to 1 minute
                    while time.time() < (timeup - 65):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " F1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " F1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 64):
                        lcd.move_to(0,0)
                        lcd.putstr("1:05 P Dn 5s   X")
                        timecurr()
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        lcd.putstr("1:04 P Dn 4s   X")
                        timecurr()
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
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        twominutelight.value(0)
                        plight.value(0)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 0 Minutes
                    while time.time() < (timeup - 5):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " F1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " F1        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 4):
                        lcd.move_to(0,0)
                        lcd.putstr("0:05 F1 Dn 5s  X")
                        timecurr()
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        lcd.putstr("0:04 F1 Dn 4s  X")
                        timecurr()
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 F1 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 F1 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 F1 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetonelight.value(0)
            if startlength == 3:
                #3 Minute Sequence
                #Check If Sequence hasn't been stopped
                if scr == "Sequence":
                    timeup = (time.time() + 180)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fleetonelight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 F1 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 2 minutes
                    while time.time() < (timeup - 125):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " F1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " F1        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 124):
                        lcd.move_to(0,0)
                        lcd.putstr("2:05 P Up 5s   X")
                        timecurr()
                    while time.time() < (timeup - 123):
                        lcd.move_to(0,0)
                        lcd.putstr("2:04 P Up 4s   X")
                        timecurr()
                    while time.time() < (timeup - 122):
                        lcd.move_to(0,0)
                        lcd.putstr("2:03 P Up 3s   X")
                        timecurr()
                    while time.time() < (timeup - 121):
                        lcd.move_to(0,0)
                        lcd.putstr("2:02 P Up 2s   X")
                        timecurr()
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        lcd.putstr("2:01 P Up 1s   X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        threeminutelight.value(0)
                        plight.value(1)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 P Up      X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 1 minute
                    while time.time() < (timeup - 65):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " F1 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " F1 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 64):
                        lcd.move_to(0,0)
                        lcd.putstr("1:05 P Dn 5s   X")
                        timecurr()
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        lcd.putstr("1:04 P Dn 4s   X")
                        timecurr()
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
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        twominutelight.value(0)
                        plight.value(0)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 0 minutes
                    while time.time() < (timeup - 5):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " F1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " F1        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 4):
                        lcd.move_to(0,0)
                        lcd.putstr("0:05 F1 Dn 5s  X")
                        timecurr()
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        lcd.putstr("0:04 F1 Dn 4s  X")
                        timecurr()
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 F1 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 F1 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 F1 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetonelight.value(0)
        if fleettwo == 1:
            #Fleet 2
            #5 Minute Sequence
            if startlength == 5:
                #Check sequence hasn't been stopped
                if scr == "Sequence":
                    timeup = (time.time() + 300)
                    #Turn on lights and sound horn
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fourminutelight.value(1)
                        fiveminutelight.value(1)
                        fleettwolight.value(1)
                    while time.time() < (timeup - 299):
                        lcd.move_to(0,0)
                        lcd.putstr("5:00 F2 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 4 Minutes
                    while time.time() < (timeup - 245):
                        lcd.move_to(0,0)
                        srem = (timeup - 240) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("4:0", srem, " F2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("4:", srem, " F2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 244):
                        lcd.move_to(0,0)
                        lcd.putstr("4:05 P Up 5s   X")
                        timecurr()
                    while time.time() < (timeup - 243):
                        lcd.move_to(0,0)
                        lcd.putstr("4:04 P Up 4s   X")
                        timecurr()
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
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        fiveminutelight.value(0)
                        plight.value(1)
                    while time.time() < (timeup - 239):
                        lcd.move_to(0,0)
                        lcd.putstr("4:00 P Up      X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 3 Minutes
                    while time.time() < (timeup - 180):
                        lcd.move_to(0,0)
                        srem = (timeup - 180) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("3:0", srem, " F2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("3:", srem, " F2 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        fourminutelight.value(0)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 F2 P      X")
                        timecurr()
                if scr == "Sequence":
                    #Countdown to 2 Minutes
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " F2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " F2 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        threeminutelight.value(0)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 F2 P      X")
                        timecurr()
                if scr == "Sequence":
                    #Countdown to 1 Minute
                    while time.time() < (timeup - 65):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " F2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " F2 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 64):
                        lcd.move_to(0,0)
                        lcd.putstr("1:05 P Dn 5s   X")
                        timecurr()
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        lcd.putstr("1:04 P Dn 4s   X")
                        timecurr()
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
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        twominutelight.value(0)
                        plight.value(0)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 0 Minutes
                    while time.time() < (timeup - 5):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " F2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " F2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 4):
                        lcd.move_to(0,0)
                        lcd.putstr("0:05 F2 Dn 5s  X")
                        timecurr()
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        lcd.putstr("0:04 F2 Dn 4s  X")
                        timecurr()
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 F2 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 F2 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 F2 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleettwolight.value(0)
            elif startlength == 3:
                #3 Minute Sequence
                #Check if sequence hasn't been stopped
                if scr == "Sequence":
                    timeup = (time.time() + 180)
                    #Operate Lights and Horn
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fleettwolight.value(1)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 F2 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 2 Minutes
                    while time.time() < (timeup - 125):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " F2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " F2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 124):
                        lcd.move_to(0,0)
                        lcd.putstr("2:05 P Up 5s   X")
                        timecurr()
                    while time.time() < (timeup - 123):
                        lcd.move_to(0,0)
                        lcd.putstr("2:04 P Up 4s   X")
                        timecurr()
                    while time.time() < (timeup - 122):
                        lcd.move_to(0,0)
                        lcd.putstr("2:03 P Up 3s   X")
                        timecurr()
                    while time.time() < (timeup - 121):
                        lcd.move_to(0,0)
                        lcd.putstr("2:02 P Up 2s   X")
                        timecurr()
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        lcd.putstr("2:01 P Up 1s   X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        threeminutelight.value(0)
                        plight.value(1)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 P Up      X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 1 Minute
                    while time.time() < (timeup - 65):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " F2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " F2 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 64):
                        lcd.move_to(0,0)
                        lcd.putstr("1:05 P Dn 5s   X")
                        timecurr()
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        lcd.putstr("1:04 P Dn 4s   X")
                        timecurr()
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
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        twominutelight.value(0)
                        plight.value(0)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 0 Minutes
                    while time.time() < (timeup - 5):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " F2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " F2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 4):
                        lcd.move_to(0,0)
                        lcd.putstr("0:05 F2 Dn 5s  X")
                        timecurr()
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        lcd.putstr("0:04 F2 Dn 4s  X")
                        timecurr()
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 F2 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 F2 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 F2 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleettwolight.value(0)
        if fleetthree == 1:
            #Fleet 3
            #5 Minute Sequence
            if startlength == 5:
                #Check if sequence hasn't been stopped
                if scr == "Sequence":
                    timeup = (time.time() + 300)
                    #Operate Lights and Horn
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fourminutelight.value(1)
                        fiveminutelight.value(1)
                        fleetthreelight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 299):
                        lcd.move_to(0,0)
                        lcd.putstr("5:00 F3 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 4 Minutes
                    while time.time() < (timeup - 245):
                        lcd.move_to(0,0)
                        srem = (timeup - 240) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("4:0", srem, " F3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("4:", srem, " F3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 244):
                        lcd.move_to(0,0)
                        lcd.putstr("4:05 P Up 3s   X")
                        timecurr()
                    while time.time() < (timeup - 243):
                        lcd.move_to(0,0)
                        lcd.putstr("4:04 P Up 4s   X")
                        timecurr()
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
                    if externallights == 1:
                        fiveminutelight.value(0)
                        plight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 239):
                        lcd.move_to(0,0)
                        lcd.putstr("4:00 P Up      X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 3 Minutes
                    while time.time() < (timeup - 180):
                        lcd.move_to(0,0)
                        srem = (timeup - 180) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("3:0", srem, " F3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("3:", srem, " F3 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        fourminutelight.value(0)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 F3 P      X")
                        timecurr()
                if scr == "Sequence":
                    #Countdown to 2 Minutes
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " F3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " F3 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        threeminutelight.value(0)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 F3 P      X")
                        timecurr()
                if scr == "Sequence":
                    #Countdown to 1 Minute
                    while time.time() < (timeup - 65):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " F3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " F3 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 64):
                        lcd.move_to(0,0)
                        lcd.putstr("1:05 P Dn 5s   X")
                        timecurr()
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        lcd.putstr("1:04 P Dn 4s   X")
                        timecurr()
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
                    if externallights == 1:
                        twominutelight.value(0)
                        plight.value(0)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 0 Minutes
                    while time.time() < (timeup - 5):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " F3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " F3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 4):
                        lcd.move_to(0,0)
                        lcd.putstr("0:05 F3 Dn 5s  X")
                        timecurr()
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        lcd.putstr("0:04 F3 Dn 4s  X")
                        timecurr()
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 F3 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 F3 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 F3 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetthreelight.value(0)
            if startlength == 3:
                #3 Minute Sequence
                #Check that Sequence hasn't been stopped
                if scr == "Sequence":
                    #Operate Lights and Horn
                    timeup = (time.time() + 180)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fleetthreelight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 F3 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 2 Minutes
                    while time.time() < (timeup - 125):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " F3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " F3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 124):
                        lcd.move_to(0,0)
                        lcd.putstr("2:05 P Up 5s   X")
                        timecurr()
                    while time.time() < (timeup - 123):
                        lcd.move_to(0,0)
                        lcd.putstr("2:04 P Up 4s   X")
                        timecurr()
                    while time.time() < (timeup - 122):
                        lcd.move_to(0,0)
                        lcd.putstr("2:03 P Up 3s   X")
                        timecurr()
                    while time.time() < (timeup - 121):
                        lcd.move_to(0,0)
                        lcd.putstr("2:02 P Up 2s   X")
                        timecurr()
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        lcd.putstr("2:01 P Up 1s   X")
                        timecurr()
                    if externallights == 1:
                        threeminutelight.value(0)
                        plight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 P Up      X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 1 Minute
                    while time.time() < (timeup - 65):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " F3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " F3 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 64):
                        lcd.move_to(0,0)
                        lcd.putstr("1:05 P Dn 5s   X")
                        timecurr()
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        lcd.putstr("1:04 P Dn 4s   X")
                        timecurr()
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
                    if externallights == 1:
                        twominutelight.value(0)
                        plight.value(0)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 58):
                        lcd.move_to(0,0)
                        lcd.putstr("1:00 P Down    X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    #Countdown to 0 Minutes
                    while time.time() < (timeup - 5):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " F3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " F3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 4):
                        lcd.move_to(0,0)
                        lcd.putstr("0:05 F3 Dn 5s  X")
                        timecurr()
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        lcd.putstr("0:04 F3 Dn 4s  X")
                        timecurr()
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 F3 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 F3 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 F3 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetthreelight.value(0)
        if rollingstart == 0:
            if fleetone == 0:
                if fleettwo == 0:
                    if fleetthree == 0:
                        scr = "Race"
            if scr == "Sequence":
                #End Sequence
                lcd.move_to(0,0)
                if externalhorn == 1:
                    horn.value(1)
                while time.time() == timeup:
                    lcd.putstr("0:00 All Dn    X")
                    timecurr()
                if externalhorn == 1:
                    horn.value(0)
                scr = "Race"
    while scr == "ABD":
        #Abandonment Menu
        lcd.move_to(0,0)
        lcd.putstr("Abandon")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= N,H     AP =>")
        if uprightbutton.value() == True:
            scr = "Race"
            time.sleep(0.2)
        elif lowrightbutton.value() == True:
            scr = "AP"
            lcd.move_to(0,1)
            lcd.putstr("AP Going Up     ")
            oneminutelight.value(1)
            threeminutelight.value(1)
            fiveminutelight.value(1)
            plight.value(1)
            fleetonelight.value(1)
            time.sleep(0.2)
            if externalhorn == 1:
                horn.value(1)
                time.sleep(1)
                horn.value(0)
                time.sleep(1)
                horn.value(1)
                time.sleep(1)
                horn.value(0)
        elif lowleftbutton.value() == True:
            scr = "NHA"
            lcd.move_to(0,1)
            lcd.putstr("N,H Going Up    ")
            oneminutelight.value(1)
            threeminutelight.value(1)
            fiveminutelight.value(1)
            plight.value(1)
            fleetonelight.value(1)
            fleettwolight.value(1)
            time.sleep(0.2)
            horn.value(1)
            time.sleep(1)
            horn.value(0)
            time.sleep(1)
            horn.value(1)
            time.sleep(1)
            horn.value(0)
            time.sleep(1)
            horn.value(1)
            time.sleep(1)
            horn.value(0)
    lcd.clear()
    while scr == "AP":
        #AP "Flag" Up
        lcd.move_to(0,0)
        lcd.putstr("AP Up")
        lcd.move_to(0,1)
        lcd.putstr("         Down =>")
        if lowrightbutton.value() == 1:
            scr = "ABD"
            lcd.move_to(0,0)
            lcd.putstr("AP Down")
            if externalhorn == 1:
                horn.value(1)
            oneminutelight.value(0)
            threeminutelight.value(0)
            fiveminutelight.value(0)
            plight.value(0)
            fleetonelight.value(0)
            if externalhorn == 1:
                time.sleep(0.5)
                horn.value(0)
            time.sleep(0.2)
    lcd.clear()
    while scr == "NHA":
        #N or H "Flag" Up
        lcd.move_to(0,0)
        lcd.putstr("N or H Up")
        lcd.move_to(0,1)
        lcd.putstr("         Down =>")
        if lowrightbutton.value() == 1:
            scr = "ABD"
            lcd.move_to(0,0)
            lcd.putstr("N or H Down")
            if externalhorn == 1:
                horn.value(1)
            oneminutelight.value(0)
            threeminutelight.value(0)
            fiveminutelight.value(0)
            plight.value(0)
            fleetonelight.value(0)
            fleettwolight.value(0)
            if externalhorn == 1:
                time.sleep(0.5)
                horn.value(0)
            time.sleep(0.2)
    lcd.clear()
    while scr == "Config1":
        #Configure Length of Start Sequence
        lcd.move_to(0,0)
        if startlength == 5:
            lcd.putstr("StartLen = 5m")
        elif startlength == 3:
            lcd.putstr("StartLen = 3m")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if startlength == 5:
                startlengthopen = open("startlength", "w")
                startlength = 3
                startlengthopen.write(str(startlength))
                startlengthopen.close()
            elif startlength == 3:
                startlengthopen = open("startlength", "w")
                startlength = 5
                startlengthopen.write(str(startlength))
                startlengthopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config2"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config2":
        #Enable or Disable Rolling (Repeating) Starts
        lcd.move_to(0,0)
        if rollingstart == 0:
            lcd.putstr("RollStrt = No ")
        elif rollingstart == 1:
            lcd.putstr("RollStrt = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if rollingstart == 0:
                rollingstartopen = open("rollingstart1", "w")
                rollingstart = 1
                rollingstartopen.write(str(rollingstart))
                rollingstartopen.close()
            elif rollingstart == 1:
                rollingstartopen = open("rollingstart1", "w")
                rollingstart = 0
                rollingstartopen.write(str(rollingstart))
                rollingstartopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config3"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config3":
        #Enable or Disable Fleet 1 Sequence
        lcd.move_to(0,0)
        if fleetone == 0:
            lcd.putstr("Fleet1 = No ")
        elif fleetone == 1:
            lcd.putstr("Fleet1 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if fleetone == 0:
                fleetoneopen = open("fleetone", "w")
                fleetone = 1
                fleetoneopen.write(str(fleetone))
                fleetoneopen.close()
            elif fleetone == 1:
                fleetoneopen = open("fleetone", "w")
                fleetone = 0
                fleetoneopen.write(str(fleetone))
                fleetoneopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config4"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config4":
        #Enable or Disable Fleet 2 Sequence
        lcd.move_to(0,0)
        if fleettwo == 0:
            lcd.putstr("Fleet2 = No ")
        elif fleettwo == 1:
            lcd.putstr("Fleet2 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if fleettwo == 0:
                fleettwoopen = open("fleettwo", "w")
                fleettwo = 1
                fleettwoopen.write(str(fleettwo))
                fleettwoopen.close()
            elif fleettwo == 1:
                fleettwoopen = open("fleettwo", "w")
                fleettwo = 0
                fleettwoopen.write(str(fleettwo))
                fleettwoopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config5"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config5":
        #Enable or Disable Fleet 3 Sequence
        lcd.move_to(0,0)
        if fleetthree == 0:
            lcd.putstr("Fleet3 = No ")
        elif fleetthree == 1:
            lcd.putstr("Fleet3 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if fleetthree == 0:
                fleetthreeopen = open("fleetthree", "w")
                fleetthree = 1
                fleetthreeopen.write(str(fleetthree))
                fleetthreeopen.close()
            elif fleetthree == 1:
                fleetthreeopen = open("fleetthree", "w")
                fleetthree = 0
                fleetthreeopen.write(str(fleetthree))
                fleetthreeopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config7"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config7":
        #Enable or Disable External Lights
        lcd.move_to(0,0)
        if externallights == 0:
            lcd.putstr("ExtLight = No ")
        elif externallights == 1:
            lcd.putstr("ExtLight = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if externallights == 0:
                externallightsopen = open("externallights", "w")
                externallights = 1
                externallightsopen.write(str(externallights))
                externallightsopen.close()
            elif externallights == 1:
                externallightsopen = open("externallights", "w")
                externallights = 0
                externallightsopen.write(str(externallights))
                externallightsopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config8"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config8":
        #Enable or Disable External Horn
        lcd.move_to(0,0)
        if externalhorn == 0:
            lcd.putstr("ExtHorn = No ")
        elif externalhorn == 1:
            lcd.putstr("ExtHorn = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if externalhorn == 0:
                externalhornopen = open("externalhorn", "w")
                externalhorn = 1
                externalhornopen.write(str(externalhorn))
                externalhornopen.close()
            elif externalhorn == 1:
                externalhornopen = open("externalhorn", "w")
                externalhorn = 0
                externalhornopen.write(str(externalhorn))
                externalhornopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config9"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config9":
        #Enable or Disable Buzzer
        lcd.move_to(0,0)
        if silent == 0:
            lcd.putstr("Silent = No ")
        elif silent == 1:
            lcd.putstr("Silent = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        if lowleftbutton.value() == True:
            time.sleep(0.2)
            if silent == 0:
                silentopen = open("silent", "w")
                silent = 1
                silentopen.write(str(silent))
                silentopen.close()
            elif silent == 1:
                silentopen = open("silent", "w")
                silent = 0
                silentopen.write(str(silent))
                silentopen.close()
        elif lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config11"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
    lcd.clear()
    while scr == "Config11":
        #Display OS Version
        lcd.move_to(0,0)
        lcd.putstr("OSVer = " + ver)
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("         Next =>")
        if lowrightbutton.value() == True:
            time.sleep(0.2)
            scr = "Config1"
        elif uprightbutton.value() == True:
            time.sleep(0.2)
            scr = "Home"
