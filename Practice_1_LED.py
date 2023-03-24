## LED 센서 ##  - 빛 출력

import RPi.GPIO as GPIO     # 센서 제어용 GPIO 모듈
import time                 # 시간 조절 모듈

GPIO.setmode(GPIO.BCM)      # 핀번호 모드 BCM 설정
GPIO.setup(18, GPIO.OUT)    # 18번 핀 OUT 설정

while True:
  try:
    GPIO.output(18, False)  # 18번 핀 Out X
    print('OFF')
    time.sleep(2)
    
    GPIO.output(18, True)   # 18번 핀 OUT O
    print('ON')
    time.sleep(2)

  # 키보드 인터럽트 발생시 ctrl + c 
  except KeyboardInterrupt:
    
    # 모든 코드 pass
    pass
    print('종료되었습니다')
    GPIO.cleanup()          # 모든 핀 자원 초기화
    exit()                  # 프로그램 종료
