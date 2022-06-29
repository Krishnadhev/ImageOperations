import cv2
img1=cv2.imread("C:/Users/kdhev/Downloads/Image Edition/star-1-300x168.jpg")
img2=cv2.imread("C:/Users/kdhev/Downloads/Image Edition/dot-300x168.jpg")
subtractedimage=cv2.subtract(img1,img2)
cv2.imwrite("subractedimage.png",subtractedimage)