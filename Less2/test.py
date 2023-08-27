import yaml
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])
user = testdata["username"]
passwd = testdata["password"]


def test_step1(x_selector_1, x_selector_2, btn_selector, x_selector_4, expected_result_1):
    input1 = site.find_element("xpath", x_selector_1)
    input1.clear()
    input1.send_keys(user)
    input2 = site.find_element("xpath", x_selector_2)
    input2.clear()
    input2.send_keys("passwd")
    btn = site.find_element("css", btn_selector)
    btn.click()
    link1 = site.find_element("xpath", x_selector_4)
    assert link1.text == expected_result_1
