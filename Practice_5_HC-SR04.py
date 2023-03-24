## 초음파 센서 ## - 거리 확인
# Trig에서 초음파를 발사하고 물체에 반사되어 돌아온 초음파를 Echo가 받는 시간을 측정한다.

import RPi.GPIO as GPIO
from time import sleep, time
 
GPIO.setmode(GPIO.BCM)      # 핀 BCM 모드 사용
 
GPIO_TRIGGER = 17           # 17번 핀
GPIO_ECHO = 18              # 18번 핀
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # 17번 핀 출력
GPIO.setup(GPIO_ECHO, GPIO.IN)      # 18번 핀 입력

 
try:
    while True:

        # 초음파 발생
        GPIO.output(GPIO_TRIGGER, True)

        sleep(0.1)
        GPIO.output(GPIO_TRIGGER, False)

        # 현재 시간으로 starttime 설정
        StartTime = time()
        StopTime = time()

        # 첫 초음파가 센서로 돌아온 시간을 StartTime으로 고정한다.
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time()      # 현재시간

        # 마지막 초음파가 센서로 들어온 시점을 stopTime으로 고정한다.
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time()       # 현재시간

        # 초음파가 처음 센서로 돌아올 때 마지막 out이 나간다. 이 마지막 out초음파에 도착 시간을 계산하여 전체 초음파 시간을 측정한다.
        TimeElapsed = StopTime - StartTime

        # 초음파 시간을 인한 거리 측정
        distance = (TimeElapsed * 34300) / 2
        print ("Measured Distance = %.1f cm" % distance)
        sleep(1)

# 키보드 인터럽트
except KeyboardInterrupt:   
    pass
    print('종료되었습니다')
    GPIO.cleanup()      # 초기화
    exit()