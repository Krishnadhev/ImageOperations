import cv2
img1=cv2.imread("C:/Users/kdhev/Downloads/Image Edition/1-500x250-3.jpg")
img2=cv2.imread("C:/Users/kdhev/Downloads/Image Edition/2-500x250-2.jpg")
addedimage=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imwrite("addedimage.png",addedimage)