
import cv2
 
orijinal_resim=cv2.imread("veri/sokak.jpg",0)

yeni_resim=cv2.resize(orijinal_resim,(640,480))

print(yeni_resim)

cv2.namedWindow("resmim",cv2.WINDOW_NORMAL)

cv2.imshow("resmim",yeni_resim)

cv2.imwrite("veri/sokak1.jpg",yeni_resim)

cv2.waitKey(0)


cv2.destroyAllWindows() 







