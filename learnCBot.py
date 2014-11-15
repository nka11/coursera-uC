import pysimulavr
from arduino import Arduino



class XPin(pysimulavr.Pin):
  def __init__(self, dev, name, state = None):
    pysimulavr.Pin.__init__(self)
    self.name = name
    if state is not None:
      self.SetPin(state)
      # hold the connecting net here, it have not be destroyed, if we leave this method
    self.__net = pysimulavr.Net()
    self.__net.Add(self)
    self.__net.Add(dev.GetPin(name))

  def SetInState(self, pin):
    pysimulavr.Pin.SetInState(self, pin)



class LearnCBot(Arduino):


  LED1  = "D4"
  LED2  = "D5"
  LED3  = "D6"
  LED4  = "D7"

  def loadDevice(self, t, e):
    device = super(LearnCBot, self).loadDevice(t, e)
    # Pull-up resistors for buttons
    self.POUS1 = XPin(device,  "D2", pysimulavr.Pin.HIGH)
    self.POUS2 = XPin(device, "D3", pysimulavr.Pin.HIGH)

    return device
