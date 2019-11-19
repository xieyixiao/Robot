# -*- coding: utf-8 -*-
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        self.video = ALProxy("ALVideoDevices")
        self.photo = ALProxy("ALPhotoCapture")
        # self.video.subscribeCamera()
        self.photo.setCameraID(0)
        self.photo.setColorSpace(0)
        self.photo.setResolution(1)
        if(not self.photo.isHalfPressEnabled):
            self.photo.setHalfPressEnabled(True)

        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        self.photo.takePicture(r"./Pic", r"Pic", True)
        self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box