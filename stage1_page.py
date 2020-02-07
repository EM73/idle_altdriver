from Idle_105.base_page import BasePage
from altunityrunner import *


class Stage1Page(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('_TestSceneBuilding')

    @property
    def base_buliding(self):
        return self.altdriver.find_object(By.PATH, '//Stage (1)/TapBuilding')

    @property
    def earn_buliding_1(self):
        return self.altdriver.find_object(By.PATH, '//Stage (1)/EarnBuilding (1)')
    @property
    def earn_buliding_2(self):

        return self.altdriver.find_object(By.PATH, '//Stage (1)/EarnBuilding (2)')
    @property
    def earn_buliding_3(self):
        return self.altdriver.find_object(By.PATH, '//Stage (1)/EarnBuilding (3)')
    @property
    def earn_buliding_4(self):
        return self.altdriver.find_object(By.PATH, '//Stage (1)/EarnBuilding (4)')
    @property
    def earn_buliding_5(self):
        return self.altdriver.find_object(By.PATH, '//Stage (1)/EarnBuilding (5)')

    def tap_base_buliding(self):
        self.base_buliding.tap()

    def tap_buliding_1(self):
        self.earn_buliding_1.tap()

    def tap_buliding_2(self):
        self.earn_buliding_2.tap()

    def tap_buliding_3(self):
        self.earn_buliding_3.tap()

    def tap_buliding_4(self):
        self.earn_buliding_4.tap()

    def tap_buliding_5(self):
        self.earn_buliding_5.tap()

    def get_building_level(self):
        

    def buildings_is_displayed(self):
        if self.base_buliding and self.earn_buliding_1 and self.earn_buliding_2 and self.earn_buliding_3 and self.earn_buliding_4 and self.earn_buliding_5:
            return True


