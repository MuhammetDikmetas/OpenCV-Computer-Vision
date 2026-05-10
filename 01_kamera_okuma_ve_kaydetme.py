import cv2

cap=cv2.VideoCapture("veri/trafik.mp4")

filename="veri/islenmis_trafik.avi"

codec=cv2.VideoWriter_fourcc('W','M','V','2')
frameRate=30
resolution=(640,480)

videofileoutput=cv2.VideoWriter(filename,codec,frameRate,resolution, isColor=False)

while True:
    
    ret,frame=cap.read()
    
    if not ret:
        break
        
    frame=cv2.resize(frame, resolution)
    
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    videofileoutput.write(frame)
    
    cv2.imshow("Trafik Analizi",frame )
    
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

videofileoutput.release()

cap.release()

cv2.destroyAllWindows()


