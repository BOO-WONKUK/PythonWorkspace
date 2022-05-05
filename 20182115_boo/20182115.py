from matplotlib.pyplot import text
import numpy as np
import cv2
import random

background = cv2.imread("20182115_boo/color.jpg", cv2.IMREAD_COLOR)     # 배경화면 영상
if background is None: raise Exception("영상파일 읽기 오류 발생")
text_mask = np.zeros((360, 480), np.uint8)                              # 검은 마스크 영상

pos_x = random.randint(5, 475)                      # 텍스트의 위치를 랜덤으로 지정
pos_y = random.randint(5, 355)
to_x = random.choice([-1, 1])                       # 텍스트의 이동방향을 랜덤으로 지정
to_y = random.choice([-1, 1])
dt = 5

fps = 29.97                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (480, 360)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DX50')            # 압축 코덱 설정
writer = cv2.VideoWriter("20182115_boo/ScreenProtect_20182115a.avi", fourcc, fps, size)      # 동영상 파일 개방 및 코덱, 해상도 설정

while True:
    text_mask.fill(0)
    cv2.putText(text_mask, 'BOOWONKUK', (pos_x, pos_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)    # 마스크 영상에 텍스트(이름) 설정
    image = cv2.bitwise_and(background , background , mask = text_mask)                     # 배경화면과 마스크 영상을 마스킹

    if pos_x <= 4 or pos_x >= 476:                  # 화면의 경계에 텍스트가 닿으면 튕겨나가도록 함
        to_x *= -1
    elif pos_y <= 4 or pos_y >= 356:
        to_y *= -1
    pos_x += to_x * dt
    pos_y += to_y * dt

    writer.write(image)                             # 프레임을 동영상으로 저장
    cv2.imshow("ScreenProtect_20182115",image)

    if cv2.waitKey(delay) == ord('q'):              # q를 입력하면 종료
        break

writer.release()
cv2.destroyAllWindows()