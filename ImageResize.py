import cv2
source="henrycavill.jpg"
destination="resizedhenrycavill.jpg"
scale_percent=50
loaded_img=cv2.imread(source, cv2.IMREAD_UNCHANGED)
new_height=int(loaded_img.shape[1]*scale_percent/100)
new_width=int(loaded_img.shape[0]*scale_percent/100)
output=cv2.resize(loaded_img,(new_height,new_width))
cv2.imwrite(destination,output)
cv2.waitKey(0)