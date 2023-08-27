import yaml
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])
user = testdata["username"]
passwd = testdata["password"]
txt = "Создан автоматически123"


def test_step1(x_selector_1, x_selector_2, btn_selector, x_selector_home1, title_home1, description_home1,
               content_home1, btn_home, expected_result_3):
    input1 = site.find_element("xpath", x_selector_1)
    input1.clear()
    input1.send_keys(user)
    input2 = site.find_element("xpath", x_selector_2)
    input2.clear()
    input2.send_keys(passwd)
    btn = site.find_element("css", btn_selector)
    btn.click()

    btn2 = site.find_element("xpath", x_selector_home1)
    btn2.click()

    input3 = site.find_element("xpath", title_home1)
    input3.send_keys(txt)
    site.pause()

    input4 = site.find_element("xpath", description_home1)
    input4.send_keys(txt)
    site.pause()

    input5 = site.find_element("xpath", content_home1)
    input5.send_keys(txt)
    site.pause()

    btn3 = site.find_element("xpath", btn_home)
    btn3.click()
    site.pause()
    text_post = site.find_element("xpath", expected_result_3)
    assert text_post.text == txt, "test1 failed"
