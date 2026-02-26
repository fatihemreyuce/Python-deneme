import cv2

kamera=cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()
    if not ret:
        print("Görüntü alınamıyor")
        break

    yukseklik,genislik,_=frame.shape

    boyut_metni = f"{yukseklik}x{genislik}"

    cv2.putText(frame,boyut_metni,(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.rectangle(frame, (100, 100), (350, 300), (0, 0, 255), 3)
    cv2.putText(frame, "Hedef Alan", (100, 90), cv2.FONT_ITALIC, 0.8, (0, 255, 255), 2)

    cv2.circle(frame, (500, 200), 60, (255, 0, 0), -1)



    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kameradan Çıkılıyor")
        break