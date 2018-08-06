from picamera import PiCamera
from time import sleep


camera = PiCamera()

camera.start_preview()

sleep(5)

for i in range(20):

	image = camera.capture('/home/pi/Desktop/image'+str(i)+'.jpg')


print(image)

camera.stop_preview()
