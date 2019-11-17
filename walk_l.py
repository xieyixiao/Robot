# -*- coding: utf-8 -*-
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        self.motion = ALProxy("ALMotion")
        # self.motion.moveInit()
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        self.motion.moveToward(0.4, 0.2, 0.0, self.motion.getMoveConfig("Default"))
        # self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box