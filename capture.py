import cv2


cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

## 비디오가 정상적으로 열렸는지 확인
def capture(date):
    ret, frame = cap.read()
    try:
        cv2.imwrite(date+'.jpg', frame)
        print("캡처완료")
        cap.release()
    except:
        print("카메라가.. 이상해..")
