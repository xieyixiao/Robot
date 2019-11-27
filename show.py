import vision_definitions
from naoqi import ALProxy
import  cv2
from PIL import Image
PORT = 9559
IP = "192.168.137.21"
camProxy = ALProxy("ALVideoDevice", IP, PORT)
photo = ALProxy("ALPhotoCapture", IP, PORT)
# video.subscribeCamera()
"""
photo.setCameraID(0)
photo.setColorSpace(0)
photo.setResolution(1)
path = r"./Pic/Pic.jpg"
"""
resolution = vision_definitions.kQVGA
colorSpace = vision_definitions.kYuvColorSpace
fps = 5
nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)

naoImage = camProxy.getImageRemote(nameId)
imageWidth = naoImage[0]
imageHeight = naoImage[1]
array = naoImage[6]
im = Image.frombytes("RGB", (imageWidth/3, imageHeight/3), array)
im.save("camImage.png", "PNG")
im2= cv2.imread("camImage.png")
cv2.imshow("dst", im2)

camProxy.unsubscribe(nameId)
"""
photo.takePicture(r"./Pic", r"Pic", True)
image = cv2.imread(path)
cv2.imshow(image)
"""
