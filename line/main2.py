#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound
from time import sleep

check_white = 0
chage_lotation = 0
cs = ColorSensor()
ul = UltrasonicSensor()
s = Sound()
tank_drive = MoveTank(left_motor_port = OUTPUT_A, right_motor_port = OUTPUT_B)
speed_change1 = 25
speed_change2 = 100

#처음에 직진
while True:
    if cs.value() < 45:
        tank_drive.on(100, 100)
    else:
        break

#라인 따라 가기
while True:
    if ul.value() < 250:
        break
    else :
        if cs.value() < 11:
            if check_white == 1:
                check_white = 0
                if chage_lotation == 0:
                    chage_lotation = 1
                else :
                    chage_lotation = 0
            else:
                if chage_lotation == 0:
                    tank_drive.on(speed_change2, 40)
                else :
                    tank_drive.on(40, speed_change2)
                # tank_drive.on(100, 100)
        elif cs.value() < 45:
            if chage_lotation == 0:
                tank_drive.on(speed_change2, 40)
            else :
                tank_drive.on(40, speed_change2)
        else :
            check_white = 1
            if chage_lotation == 0:
                tank_drive.on(speed_change1, speed_change2)
            else :
                tank_drive.on(speed_change2, speed_change1)
    if ul.value() < 600:
        speed_change1 = 10
        speed_change2 = 80

#벽으로 가다가 멈추기
while True:
    if ul.value() < 100:
        tank_drive.on(10, 10)
        if ul.value() < 31:
            tank_drive.on_for_seconds(10, 10, 0.2)
            tank_drive.off()
            break
    else :
        tank_drive.on(100, 100)

s.speak("hey! this is my class ha! ha!")