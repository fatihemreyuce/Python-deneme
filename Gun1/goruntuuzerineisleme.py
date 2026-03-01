import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
onceki_zaman = time.time()
while True:
    ret, frame = cam.read()
    if not ret:
        print("Kamera açılamıyor")
        break
    suanki_zaman = time.time()
    gecen_sure = suanki_zaman - onceki_zaman
    if gecen_sure>0:
        fps=1/gecen_sure
    else:
        fps=0
    onceki_zaman = suanki_zaman
    fps_metni = f"FPS: {int(fps)}"

    cv2.putText(frame,fps_metni,(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.rectangle(frame,(20,100),(350,300),(150,100,200),3)
    cv2.putText(frame,"Hedef Bolge",(20,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.circle(frame, (500, 200), 60, (120, 100, 20), 3)


    cv2.imshow("Kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kameradan çıkılıyor...")
        break
cam.release()
cv2.destroyAllWindows()
