import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
import cvzone


cap = cv.VideoCapture(0)



while True:
    success, img = cap.read()

    if not success:
        break

    for code in decode(img):
        decoded_data = code.data.decode("utf-8")

        rect_pts = code.rect


        if decoded_data:
            pts = np.array([code.polygon], np.int32)
            cv.polylines(img, [pts], True, (0,255,0), 3)
            #cv.putText(img, str(decoded_data), (rect_pts[0], rect_pts[1]), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0),2)
            cvzone.putTextRect(img, str(decoded_data), (rect_pts[0], rect_pts[1]),  scale=2, thickness=2, border=2)


    cv.imshow("Qrcode", img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

