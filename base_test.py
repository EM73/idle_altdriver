import os
import sys

sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltrunUnityDriver
import unittest
import pytest
from appium import webdriver

class TestBase(unittest.TestCase):
    plaform = os.getenv('TESTS_PLATFORM', 'android')

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['deviceName'] = 'Galaxy J7 (2016)'
        cls.desired_caps['app'] = '/Users/mac/idle_1.0v5/altidle_105/altIdle.apk'
        cls.desired_caps['appPackage'] = 'com.tbegames.and.cityClicker'

        #self.desired_caps['adbPort'] = 13002
        #self.desired_caps['systemPort'] = 8201
        #self.desired_caps['automationName'] = 'Appium'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        cls.altdriver = AltrunUnityDriver(cls.driver, platform='android')

    @classmethod    
    def tearDownClass(cls):
        cls.altdriver.stop()