import os
import cv2
cap = cv2.VideoCapture(0)
directory = 'Images/'
while True:
    _,frame = cap.read()
    count = {
        'hello' : len(os.listdir(directory+"Hello")),
        'yes' : len(os.listdir(directory+"Yes")),
        'no' : len(os.listdir(directory+"No")),
        'thanks' : len(os.listdir(directory+"Thanks")),
        'iloveyou' : len(os.listdir(directory+"IloveYou")),
    }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame = frame[40:400,0:300]
    interrupt = cv2.waitKey(10)

    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'Hello/'+str(count['hello'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'Yes/'+str(count['yes'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'No/'+str(count['no'])+'.png',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'Thanks/'+str(count['thanks'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'ILoveYou/'+str(count['iloveyou'])+'.png',frame)

cap.release()
cv2.destroyAllWindows()