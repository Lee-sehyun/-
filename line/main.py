#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sound import Sound
from time import sleep

check_white = 0
chage_lotation = 0
cs = ColorSensor(INPUT_4)
ul = UltrasonicSensor(INPUT_3)
tank_drive = MoveTank(left_motor_port = OUTPUT_A, right_motor_port = OUTPUT_B)

#라인 따라 가기
while True:
    if ul.distance_centimeters() < 60:
        break
    else :
        if cs.ambient_light_intensity < 30:
            if check_white == 1:
                check_white = 0
                if chage_lotation == 0:
                    chage_lotation = 1
                else :
                    chage_lotation = 0
            else:
                tank_drive.on(100, 100)
        else :
            check_white = 1
            if chage_lotation == 0:
                tank_drive.on(50, 100)
            else :
                tank_drive.on(100, 50)

#벽을 만나 검정색을 만나기까지 와리가리
while True:
    if cs.ambient_light_intensity < 30 and ul.distance_centimeters() < 50:
        break
    else :
        if chage_lotation == 0:
            if cs.ambient_light_intensity < 30:
                tank_drive.on(50, 100)
            else :
                tank_drive.on(100, 50)
        else:
            if cs.ambient_light_intensity < 30:
                tank_drive.on(100, 50)
            else :
                tank_drive.on(50, 100)

#벽으로 가다가 멈추기
while True:
    if ul.distance_centimeters() < 3:
        tank_drive.on(10, 10)
        if ul.distance_centimeters() < 0.3:
            tank_drive.off()
            break #여기 한 번 확인 해야할 것 같음.
    else :
        tank_drive.on(100, 100)

# Sound.speak("hey! this is my class ha! ha!")