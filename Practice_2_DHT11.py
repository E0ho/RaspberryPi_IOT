## 온도 습도 센서 DHT11 ## - 온도 습도 측정

import time              # 시간 조절 모듈
import board             # 데이터를 송신하는 모듈
import adafruit_dht      # DHT 센서를 이용하기 위한 모듈

# 18번 핀을 DHT11로 사용하겠다.
dhtDevice = adafruit_dht.DHT11(board.D18)

while True:
    try:
        # 섭씨 온도 데이터 가져오기
        temperature_c = dhtDevice.temperature
        # 화씨 온도 데이터로 변환
        temperature_f = temperature_c * (9 / 5) + 32
        # 습도 데이터 가져오기
        humidity = dhtDevice.humidity
        
        # 출력
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity))
        
        # 2초 대기
        time.sleep(2.0)

  # 키보드 인터럽트 발생시 ctrl + c 
  except KeyboardInterrupt:

    # 모든 코드 pass
    pass

    print('종료되었습니다')

    exit()          # 프로그램 종료
