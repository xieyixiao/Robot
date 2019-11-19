# ~ This script was generated automatically by drang&drop from Position Library
class MyClass(GeneratedClass):
    def __init__(self):
        try:  # disable autoBind
            GeneratedClass.__init__(self, False)
        except TypeError:  # if NAOqi < 1.14
            GeneratedClass.__init__(self)

    def onLoad(self):
        # self.postureProxy = ALProxy("ALRobotPosture")
        self.motionProxy = ALProxy("ALMotion")

    def onUnload(self):

    def onInput_onStart(self):
        self.motionProxy.moveInit()
        self.motionProxy.wbEnableEffectorControl("Head", True)
        self.motionProxy.wbSetEffectorControl("Head", [0.0, 0.5, 0.0])
        self.motionProxy.wbEnableEffectorControl("Head", False)
        self.onStopped()


    def onInput_onStop(self):
        self.onUnload()  # ~ it is recommanded to call onUnload of this box in a onStop method,               as the code written in onUnload is used to stop the box as well
     pass
