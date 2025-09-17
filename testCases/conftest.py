from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Lunching Chrome Browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Lunching Firefox browser")
    else:
        driver = webdriver.Ie() #by defualt browser
    return driver

def pytest_addoption(parser): # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")


###### pytest HTML Report #####
# it is hook for Adding Enviroment info to HTML Report
import pytest

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Add custom info
    metadata["Project Name"] = "nop Commerce"
    metadata["Module Name"] = "customers"
    metadata["Tester"] = "Sudama"

    # Remove unwanted default keys
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

