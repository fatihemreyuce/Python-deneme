import cv2
import time

cam = cv2.VideoCapture(0)
onceki_zaman=time.time()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Kamera Açılamadı")
        break
    suanki_Zaman=time.time()
    gecen_sure= suanki_Zaman - onceki_zaman
    if gecen_sure>0:
        fps = 1/gecen_sure
    else:
        fps = 0
    onceki_zaman = suanki_Zaman
    fps_metni=f"FPS: {int(fps)}"

    cv2.putText(frame,fps_metni,(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kameradan Çıkılıyor...")
        break
cam.release()
cv2.destroyAllWindows()