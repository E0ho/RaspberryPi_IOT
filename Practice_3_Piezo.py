## 피에조 센서 ## - 소리 출력

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)     # 경고 문구 제거
GPIO.setmode(GPIO.BCM)      # 핀번호 모드 BCM 설정

buzzer = 17
GPIO.setup(buzzer,GPIO.OUT) # 17번핀을 출력으로 사용

while True:
    try:

        # 17번 핀 output에 True 입력
        GPIO.output(buzzer,GPIO.HIGH)       # GPIO.HIGH = True
        print ("Beep")
        sleep(0.5)
        
        # 17번 핀 output False
        GPIO.output(buzzer,GPIO.LOW)        # GPIO.LOW = False
        print ("No Beep")
        sleep(0.5)

    # 키보드 인터럽트 발생
    except KeyboardInterrupt:

        pass
        print('종료되었습니다')
        GPIO.cleanup()      # 핀 설정 초기화
        exit()              # 종료
