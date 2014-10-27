#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Python test script as demonstration of using pysimulavr in unit tests
from unittest import TestSuite, TextTestRunner, TestCase, defaultTestLoader
from sys import argv

import pysimulavr
from atmega328 import ATMega328

class Arduino(TestCase, ATMega328):
  
  def setUp(self):
    self.device = self.loadDevice("atmega328", "ex1.elf")
    
  def tearDown(self):
    del self.device
    
  def testLED13(self):
    import time
    "test toggle output pin (portB7)"
    o = 10000   # duration of interrupt function, about 10us
    d = 1000000000 #1sec timer
    # now output should be set to LOW
    print "%s %s" % (self.getCurrentTime(),self.device.GetPin("B5").toChar())
    self.doRun(d * 2) # wait 5 secs for init
    print "%s %s" % (self.getCurrentTime(),self.device.GetPin("B5").toChar())
    lastval = self.device.GetPin("B5").toChar()
    for x in range(3,10): # Test 10 times state switching on PORTB-5
      self.doRun(d * x)
      curval = self.device.GetPin("B5").toChar()
      self.assertNotEqual(lastval,curval)
      lastval = curval

        
if __name__ == "__main__":
  allTestsFrom = defaultTestLoader.loadTestsFromTestCase
  suite = TestSuite()
  suite.addTests(allTestsFrom(Arduino))
  TextTestRunner(verbosity = 2).run(suite)

  #sim = Arduino()
  #sim.init()
  #sim.testLED13()
  #sim.finish() 
