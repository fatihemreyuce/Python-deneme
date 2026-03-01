import cv2

kamera = cv2.VideoCapture(0)
ret, frame = kamera.read()
if ret:
    print("Açılan pencerede fare ile bir bölge secin ve ENTER tuşuna basınız")

    secim = cv2.selectROI("Bölge Seç",frame)


    x,y,w,h = secim
    print(f"Secilen Koordinatlar X:{x},Y:{y},W:{w},H:{h}")

    if w>0 and h>0:
        roi_bolgesi = frame[y:y+h,x:x+w]
        cv2.imshow("Kesilen ROI bölgesi",roi_bolgesi)

        cv2.waitKey(0)
    else:
        print("Herhangi bir alan seçmediniz")

kamera.release()
cv2.destroyAllWindows()