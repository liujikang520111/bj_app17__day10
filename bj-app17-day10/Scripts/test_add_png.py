import os

import allure


class TestAddPng:
    def test_001(self):
        with open("./lmage" + os.sep + "hh.bmp", "rb")as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        assert True
