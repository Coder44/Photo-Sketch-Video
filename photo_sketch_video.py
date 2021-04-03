import cv2
#the function below is for finding the boldest edges of the image by diving the graysacle image by the image_smoothing and giving the proper result.
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)
video = cv2.VideoCapture(0) #live video capture

#to work on each frame and convert it and display it live to the user.
while True:
	_, img = video.read() #reading the images/frames of the video
	grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting it to grayscale
	bitwise = cv2.bitwise_not(grayscale) #this is needed because it will make the lighter parts darker and vice versa.
	blur = cv2.GaussianBlur(bitwise, (21,21), sigmaX=0, sigmaY=0) #this is used to smoothen the image and apply the lines in our photo

	final_image = dodgeV2(grayscale, blur) #here we are using the function to find the boldest edges of the image and apply the sketch lines.
	cv2.imshow('img', final_image)
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break
video.release()