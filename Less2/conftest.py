import  pytest
import  yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

user = testdata["username"]
passwd = testdata["password"]

@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def x_selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def btn_selector():
     return "button"

@pytest.fixture()
def expected_result_1():
     return "401"

@pytest.fixture()
def x_selector_4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def expected_result_2():
    return f"Hello, {user}"

@pytest.fixture()
def x_selector_home1():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def title_home1():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def description_home1():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def content_home1():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def btn_home():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def expected_result_3():
     return """//*[@id="app"]/main/div/div[1]/h1"""
