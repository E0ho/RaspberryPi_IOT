## 피에조 센서 ## - 소리 출력

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 17

# 도레미파솔라시도 초음파 숫자
scales = [261, 294, 329, 349, 392, 440, 493, 523]

# 17번 핀 출력으로 사용
GPIO.setup(buzzer,GPIO.OUT) 

# 디지털을 아날로그로 변환 (펄스길이 600으로 변환 -> 소리가 커진다.)
p = GPIO.PWM(buzzer, 600)       # PWM 파형으로 주파수를 출력한다.

# 피에조 센서에서 음계를 출력하기 위한 기본 코드
p.start(50)

try:
	for scale in scales:
		
        # 주파수 변환
		p.ChangeFrequency(scale)
		sleep(0.5)

# 키보드 인터럽트 발생
except KeyboardInterrupt:
	
	pass
	print('종료되었습니다.')
	GPIO.cleanup()      # 핀 초기화
	exit()              # 종료
