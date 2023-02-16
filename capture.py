import cv2

from picamera2 import Picamera2

#cv2.startWindowThread()

picam2 = Picamera2()
print(picam2.camera_properties)
config = picam2.create_preview_configuration(main={"size": (800, 800), "format": "RGB888"})
picam2.configure(config)
picam2.image_effect = "none"
picam2.start()

img = picam2.capture_array("main")
#img = cv2.cvtColor(img, cv2.COLOR_YUV420p2RGB)

cv2.imwrite("test.jpg", img)
