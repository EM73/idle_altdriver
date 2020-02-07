from Idle_105.stage1_page import Stage1Page
from Idle_105.base_test import TestBase
from altunityrunner import *

class TestStage1Page(TestBase):
    
    def setUp(self):
        self.stage1_page = Stage1Page(self.altdriver)
        self.stage1_page.load()


    def test_stage1_loaded_correctly(self):
        assert(self.stage1_page.buildings_is_displayed())
    
    def test_tap_all_building(self):
        for i in range(3):
            self.stage1_page.tap_buliding_1()
            for j in range(5):
                self.stage1_page.tap_base_buliding()

        assert(self.stage1_page.buildings_is_displayed())

