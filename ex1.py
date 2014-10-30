#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Python test script as demonstration of using pysimulavr in unit tests
from unittest import TestSuite, TextTestRunner, TestCase, defaultTestLoader
from sys import argv

import pysimulavr
from arduino import Arduino

class TestExerciceSemaine1(TestCase, Arduino):
  
  def setUp(self):
    self.device = self.loadDevice("atmega328", "ex1.elf")
    
  def tearDown(self):
    del self.device
    
  def testLED13(self):
    import time
    "test toggle output pin (portB7)"
    d = 1000000000 #1sec timer
    self.doRun(1000000) # startup
    lastval = self.device.GetPin(self.PIN13LED).toChar()
    for x in range(1,10): # Test 10 times state switching on PORTB-5
      self.doRun(d)
      curval = self.device.GetPin(self.PIN13LED).toChar()
      self.assertNotEqual(lastval,curval)
      lastval = curval

        
if __name__ == "__main__":
  allTestsFrom = defaultTestLoader.loadTestsFromTestCase
  suite = TestSuite()
  suite.addTests(allTestsFrom(TestExerciceSemaine1))
  TextTestRunner(verbosity = 2).run(suite)

