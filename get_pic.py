class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        self.video = ALProxy("ALVideoDevices")
        self.photo = ALProxy("ALPhotoCapture")
        self.photo.setCameraID(0)
        self.photo.setColorSpace(0)

        self.photo.setPictureFormat("jpg")
        self.photo.setHalfPressEnabled(True)
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box