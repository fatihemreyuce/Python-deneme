import cv2

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    if not ret:
        print("Kamera Açılamadı")
        break
    yukseklik,genislik,_ = frame.shape

    boyut_metni = f"{genislik} {yukseklik}"

    cv2.putText(frame, boyut_metni, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Goruntu",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kameradan çıkış yapılıyor")
        break