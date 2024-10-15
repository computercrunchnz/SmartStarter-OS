ver = "1.0B1"

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

lowrightbutton = Pin(2, Pin.IN)
uprightbutton = Pin(3, Pin.IN)
lowleftbutton = Pin(4, Pin.IN)
upleftbutton = Pin(5, Pin.IN)
hornbutton = Pin(28, Pin.IN)
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
            time.sleep(0.2)
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
            elif second == 56:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 57:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 58:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 59:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            elif second == 00:
                if silent == 0:
                    buz.duty_u16(3500)
                    time.sleep(0.2)
                    buz.duty_u16(000)
            while lowleftbutton.value() == True:
                if externalhorn == 1:
                    horn.value(1)
                if silent == 0:
                    buz.duty_u16(3500)
            if externalhorn == 1:
                horn.value(0)
            if silent == 0:
                buz.duty_u16(000)
            while hornbutton.value() == True:
                if externalhorn == 1:
                    horn.value(1)
                if hornbutton.value() == False:
                    horn.value(0)
        while scr == "Sequence":
            time.sleep(0.2)
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
                if time.time() == (timeup - 243):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 242):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 241):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 240):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 63):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 62):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 61):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 60):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 3):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 2):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 1):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == timeup:
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
            elif startlength == 3:
                if time.time() == (timeup - 123):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 122):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 121):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 120):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 63):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 62):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 61):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 60):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 3):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 2):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == (timeup - 1):
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
                elif time.time() == timeup:
                    if silent == 0:
                        buz.duty_u16(3500)
                        time.sleep(0.2)
                        buz.duty_u16(000)
            
            while lowleftbutton.value() == True:
                if externalhorn == 1:
                    horn.value(1)
                if silent == 0:
                    buz.duty_u16(3500)
            if externalhorn == 1:
                horn.value(0)
            if silent == 0:
                buz.duty_u16(000)
        else:
            while hornbutton.value() == True:
                if externalhorn == 1:
                    horn.value(1)
                if hornbutton.value() == False:
                    horn.value(0)

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
        time.sleep(0.3)
        if lowleftbutton.value() == True:
            scr = "Home"
        elif lowrightbutton.value() == True:
            scr = "Time1"
            tm = rtc.datetime()
            year = tm[0]
            month = tm[1]
            day = tm[2]
            hour = tm[4]
            minute = tm[5]
            second = tm[6]
        if uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Time1":
        #Set Year
        lcd.move_to(0,0)
        lcd.putstr("<= Up  Year:" + str(year))
        lcd.move_to(0,1)
        lcd.putstr("<= Down  Next =>")
        time.sleep(0.3)
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
        time.sleep(0.3)
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
        time.sleep(0.3)
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
        time.sleep(0.3)
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
        time.sleep(0.3)
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
        lcd.putstr("<= Set0  Exit =>")
        time.sleep(0.3)
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
        time.sleep(0.3)
        if upleftbutton.value() == True:
            scr = "Race"
        if lowleftbutton.value() == True:
            if dispon == 1:
                lcd.backlight_off()
                dispon = 0
            elif dispon == 0:
                lcd.backlight_on()
                dispon = 1
        if lowrightbutton.value() == True:
            scr = "Config1"
        elif uprightbutton.value() == True:
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
        time.sleep(0.3)
        if upleftbutton.value() == True:
            scr = "Start"
        while lowleftbutton.value() == True:
            if silent == 0:
                buz.duty_u16(3500)
            if externalhorn == 1:
                horn.value(1)
        if silent == 0:
            buz.duty_u16(000)
        if externalhorn == 1:
            horn.value(0)
        if uprightbutton.value() == True:
            scr = "Home"
        elif lowrightbutton.value() == True:
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
        if uprightbutton.value() == True:
            scr = "Home"
            time.sleep(0.3)
    while scr == "Start":
        if fleetone == 1:
            start = 1
        elif fleettwo == 1:
            start = 1
        elif fleetthree == 1:
            start = 1
        else:
            start = 0
        if start == 1:
            if waitbeforestart == 1:
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
                if startlength == 5:
                    lcd.putstr("05:00")
                elif startlength == 3:
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
                if uprightbutton.value() == True:
                    scr = "Race"
                    time.sleep(0.3)
            else:
                scr = "Sequence"
        else:
            lcd.move_to(0,0)
            lcd.putstr("Error! Must have")
            lcd.move_to(0,1)
            lcd.putstr("fleet! Chk conf.")
            time.sleep(2)
            scr = "Race"
    while scr == "Sequence":
        if fleetone == 1:
            if startlength == 5:
                if scr == "Sequence":
                    timeup = (time.time() + 300)
                    if externalhorn == 1:
                        horn.value(1)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fourminutelight.value(1)
                        fiveminutelight.value(1)
                        fleetonelight.value(1)
                    while time.time() < (timeup - 298):
                        lcd.move_to(0,0)
                        lcd.putstr("5:00 C1 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
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
                    if externallights == 1:
                        fourminutelight.value(0)
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
                    if externallights == 1:
                        threeminutelight.value(0)
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
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C1        X")
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
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetonelight.value(0)
            if startlength == 3:
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
                        lcd.putstr("3:00 C1 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 123):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " C1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " C1        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
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
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C1        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C1        X")
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
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetonelight.value(0)
        if fleettwo == 1:
            if startlength == 5:
                if scr == "Sequence":
                    timeup = (time.time() + 300) 
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fourminutelight.value(1)
                        fiveminutelight.value(1)
                        fleettwolight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 299):
                        lcd.move_to(0,0)
                        lcd.putstr("5:00 C2 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 243):
                        lcd.move_to(0,0)
                        srem = (timeup - 240) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("4:0", srem, " C2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("4:", srem, " C2        X")
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
                    while time.time() < (timeup - 180):
                        lcd.move_to(0,0)
                        srem = (timeup - 180) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("3:0", srem, " C2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("3:", srem, " C2 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        fourminutelight.value(0)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 C2 P      X")
                        timecurr()
                if scr == "Sequence":
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " C2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " C2 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        threeminutelight.value(0)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 C2 P      X")
                        timecurr()
                if scr == "Sequence":
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " C2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " C2 P      X")
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
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 C2 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 C2 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 C2 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleettwolight.value(0)
            elif startlength == 3:
                if scr == "Sequence":
                    timeup = (time.time() + 180)
                    if externallights == 1:
                        oneminutelight.value(1)
                        twominutelight.value(1)
                        threeminutelight.value(1)
                        fleettwolight.value(1)
                    if externalhorn == 1:
                        horn.value(1)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 C2 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 123):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " C2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " C2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
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
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " C2 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " C2 P      X")
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
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C2        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C2        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 C2 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 C2 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 C2 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleettwolight.value(0)
        if fleetthree == 1:
            if startlength == 5:
                if scr == "Sequence":
                    timeup = (time.time() + 300)
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
                        lcd.putstr("5:00 C2 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 243):
                        lcd.move_to(0,0)
                        srem = (timeup - 240) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("4:0", srem, " C3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("4:", srem, " C3        X")
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
                    while time.time() < (timeup - 180):
                        lcd.move_to(0,0)
                        srem = (timeup - 180) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("3:0", srem, " C3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("3:", srem, " C3 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        fourminutelight.value(0)
                    while time.time() < (timeup - 179):
                        lcd.move_to(0,0)
                        lcd.putstr("3:00 C3 P      X")
                        timecurr()
                if scr == "Sequence":
                    while time.time() < (timeup - 120):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " C3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " C3 P      X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    if externallights == 1:
                        threeminutelight.value(0)
                    while time.time() < (timeup - 119):
                        lcd.move_to(0,0)
                        lcd.putstr("2:00 C3 P      X")
                        timecurr()
                if scr == "Sequence":
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " C3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " C3 P      X")
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
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 C3 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 C3 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 C3 Dn 1s  X")
                        timecurr()
                    if externallights == 1:
                        oneminutelight.value(0)
                        fleetthreelight.value(0)
            if startlength == 3:
                if scr == "Sequence":
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
                        lcd.putstr("3:00 C3 Up     X")
                        timecurr()
                    if externalhorn == 1:
                        horn.value(0)
                if scr == "Sequence":
                    while time.time() < (timeup - 123):
                        lcd.move_to(0,0)
                        srem = (timeup - 120) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("2:0", srem, " C3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("2:", srem, " C3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
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
                    while time.time() < (timeup - 63):
                        lcd.move_to(0,0)
                        srem = (timeup - 60) - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("1:0", srem, " C3 P      X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("1:", srem, " C3 P      X")
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
                    while time.time() < (timeup - 3):
                        lcd.move_to(0,0)
                        srem = timeup - time.time()
                        if srem < 10:
                            trem = '{}{}{}'.format("0:0", srem, " C3        X")
                            lcd.putstr(trem)
                        else:
                            trem = '{}{}{}'.format("0:", srem, " C3        X")
                            lcd.putstr(trem)
                        timecurr()
                        if scr == "Race":
                            break
                if scr == "Sequence":
                    while time.time() < (timeup - 2):
                        lcd.move_to(0,0)
                        lcd.putstr("0:03 C3 Dn 3s  X")
                        timecurr()
                    while time.time() < (timeup - 1):
                        lcd.move_to(0,0)
                        lcd.putstr("0:02 C3 Dn 2s  X")
                        timecurr()
                    while time.time() < timeup:
                        lcd.move_to(0,0)
                        lcd.putstr("0:01 C3 Dn 1s  X")
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
                lcd.move_to(0,0)
                if externalhorn == 1:
                    horn.value(1)
                while time.time() == timeup:
                    lcd.putstr("0:00           X")
                    timecurr()
                time.sleep(1)
                if externalhorn == 1:
                    horn.value(0)
                scr = "Race"
    while scr == "ABD":
        lcd.move_to(0,0)
        lcd.putstr("Abandon")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= N,H     AP =>")
        time.sleep(0.3)
        if uprightbutton.value() == True:
            scr = "Race"
        elif lowrightbutton.value() == True:
            scr = "AP"
            lcd.move_to(0,1)
            lcd.putstr("AP Going Up     ")
            if externalhorn == 1:
                horn.value(1)
                time.sleep(1)
                horn.value(0)
                time.sleep(0.5)
                horn.value(1)
                time.sleep(1)
                horn.value(0)
        elif lowleftbutton.value() == True:
            scr = "NHA"
            horn.value(1)
            time.sleep(1)
            horn.value(0)
            time.sleep(0.5)
            horn.value(1)
            time.sleep(1)
            horn.value(0)
            time.sleep(0.5)
            horn.value(1)
            time.sleep(1)
            horn.value(0)
    lcd.clear()
    while scr == "AP":
        lcd.move_to(0,0)
        lcd.putstr("AP Up")
        lcd.move_to(0,1)
        lcd.putstr("<= Horn  Down =>")
        oneminutelight.value(1)
        threeminutelight.value(1)
        fiveminutelight.value(1)
        plight.value(1)
        fleetonelight.value(1)
        time.sleep(0.3)
        while lowleftbutton.value() == 1:
            horn.value(1)
            bz()
            horn.value(0)
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
    lcd.clear()
    while scr == "NHA":
        lcd.move_to(0,0)
        lcd.putstr("N or H Up")
        lcd.move_to(0,1)
        lcd.putstr("<= Horn  Down =>")
        oneminutelight.value(1)
        threeminutelight.value(1)
        fiveminutelight.value(1)
        plight.value(1)
        fleetonelight.value(1)
        fleettwolight.value(1)
        time.sleep(0.3)
        while lowleftbutton.value() == 1:
            horn.value(1)
            bz()
            horn.value(0)
        if lowrightbutton.value() == 1:
            scr = "ABD"
            oneminutelight.value(0)
            threeminutelight.value(0)
            fiveminutelight.value(0)
            plight.value(0)
            fleetonelight.value(0)
            fleettwolight.value(0)
    lcd.clear()
    while scr == "Config1":
        lcd.move_to(0,0)
        if startlength == 5:
            lcd.putstr("StartLen = 5m")
        elif startlength == 3:
            lcd.putstr("StartLen = 3m")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config2"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config2":
        lcd.move_to(0,0)
        if rollingstart == 0:
            lcd.putstr("RollStrt = No ")
        elif rollingstart == 1:
            lcd.putstr("RollStrt = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
            if rollingstart == 0:
                rollingstartopen = open("rollingstart1", "w")
                rollingstart = 1
                rollingstartopen.write(str(startlength))
                rollingstartopen.close()
            elif rollingstart == 1:
                rollingstartopen = open("rollingstart1", "w")
                rollingstart = 0
                rollingstartopen.write(str(rollingstart))
                rollingstartopen.close()
            else:
                rollingstartopen = open("rollingstart1", "w")
                rollingstart = 0
                rollingstartopen.write(str(rollingstart))
                rollingstartopen.close()
        elif lowrightbutton.value() == True:
            scr = "Config3"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config3":
        lcd.move_to(0,0)
        if fleetone == 0:
            lcd.putstr("Fleet1 = No ")
        elif fleetone == 1:
            lcd.putstr("Fleet1 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config4"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config4":
        lcd.move_to(0,0)
        if fleettwo == 0:
            lcd.putstr("Fleet2 = No ")
        elif fleettwo == 1:
            lcd.putstr("Fleet2 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config5"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config5":
        lcd.move_to(0,0)
        if fleetthree == 0:
            lcd.putstr("Fleet3 = No ")
        elif fleetthree == 1:
            lcd.putstr("Fleet3 = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config6"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config6":
        lcd.move_to(0,0)
        if waitbeforestart == 0:
            lcd.putstr("StrOnMin = No ")
        elif waitbeforestart == 1:
            lcd.putstr("StrOnMin = Yes ")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
            if waitbeforestart == 0:
                waitbeforestartopen = open("waitbeforestart", "w")
                waitbeforestart = 1
                waitbeforestartopen.write(str(waitbeforestart))
                waitbeforestartopen.close()
            elif waitbeforestart == 1:
                waitbeforestartopen = open("waitbeforestart", "w")
                waitbeforestart = 0
                waitbeforestartopen.write(str(waitbeforestart))
                waitbeforestartopen.close()
        elif lowrightbutton.value() == True:
            scr = "Config7"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config7":
        lcd.move_to(0,0)
        if externallights == 0:
            lcd.putstr("ExtLight = No ")
        elif externallights == 1:
            lcd.putstr("ExtLight = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config8"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config8":
        lcd.move_to(0,0)
        if externalhorn == 0:
            lcd.putstr("ExtHorn = No ")
        elif externalhorn == 1:
            lcd.putstr("ExtHorn = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config9"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config9":
        lcd.move_to(0,0)
        if silent == 0:
            lcd.putstr("Silent = No ")
        elif silent == 1:
            lcd.putstr("Silent = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
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
            scr = "Config10"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config10":
        lcd.move_to(0,0)
        if lighttest == 0:
            lcd.putstr("LightTest = No ")
        elif lighttest == 1:
            lcd.putstr("LightTest = Yes")
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("<= Set   Next =>")
        time.sleep(0.3)
        if lowleftbutton.value() == True:
            if lighttest == 0:
                lighttest = 1
                oneminutelight.value(1)
                twominutelight.value(1)
                threeminutelight.value(1)
                fourminutelight.value(1)
                fiveminutelight.value(1)
                fleetonelight.value(1)
                fleettwolight.value(1)
                fleetthreelight.value(1)
                plight.value(1)
            elif lighttest == 1:
                lighttest = 0
                oneminutelight.value(0)
                twominutelight.value(0)
                threeminutelight.value(0)
                fourminutelight.value(0)
                fiveminutelight.value(0)
                fleetonelight.value(0)
                fleettwolight.value(0)
                fleetthreelight.value(0)
                plight.value(0)
            time.sleep(1)
        elif lowrightbutton.value() == True:
            scr = "Config11"
        elif uprightbutton.value() == True:
            scr = "Home"
    lcd.clear()
    while scr == "Config11":
        lcd.move_to(0,0)
        lcd.putstr("OSVer = " + ver)
        lcd.move_to(15,0)
        lcd.putchar("X")
        lcd.move_to(0,1)
        lcd.putstr("         Next =>")
        time.sleep(0.3)
        if lowrightbutton.value() == True:
            scr = "Config1"
        elif uprightbutton.value() == True:
            scr = "Home"
