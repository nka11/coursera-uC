from unittest.case import TestCase
from unittest.loader import defaultTestLoader
from unittest.runner import TextTestRunner
from unittest.suite import TestSuite
import pysimulavr

from learnCBot import LearnCBot


__author__ = 'nico'


class TestEx1Semaine2(TestCase, LearnCBot):

  def setUp(self):
    self.device = self.loadDevice("atmega328", "s2ex1.elf")

  def tearDown(self):
    del self.device

  def testPushButton(self):
    d = 1000000000 #1sec timer
    self.doRun(1000000) # startup
    assert(self.device.GetPin(self.LED1).toChar() == "L")
    assert(self.device.GetPin(self.LED2).toChar() == "L")
    self.POUS1.SetInState(pysimulavr.Pin.LOW)
    self.doRun(2500000) # 25ms // temps de pression
    self.device.POUS2.SetInState(self.device.POUS2.HIGH) # relache
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "L")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "L")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "L")
    self.doRun(2500000) # 25ms
    # Premiere seconde, les diodes changent d'etat (11)
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "H")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    # Deuxieme seconde
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "L")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "L")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "L")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "L")
    assert(self.device.GetPin(self.LED2).toChar() == "H")
    self.doRun(2500000) # 25ms
    assert(self.device.GetPin(self.LED1).toChar() == "L")
    assert(self.device.GetPin(self.LED2).toChar() == "L")



if __name__ == "__main__":
  allTestsFrom = defaultTestLoader.loadTestsFromTestCase
  suite = TestSuite()
  suite.addTests(allTestsFrom(TestEx1Semaine2))
  TextTestRunner(verbosity = 2).run(suite)

