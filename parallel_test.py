from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import selenium_assignment
import os

build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

def win_chrome_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.14.0",
    },
    "browserName" : "Chrome",
    "browserVersion" : "latest",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)

def mac_chrome_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "OS X",
        "osVersion" : "Big Sur",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.14.0",
    },
    "browserName" : "Chrome",
    "browserVersion" : "latest",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)

def win_firefox_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.10.0",
    },
    "browserName" : "Firefox",
    "browserVersion" : "latest",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)

def mac_firefox_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "OS X",
        "osVersion" : "Big Sur",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.10.0",
    },
    "browserName" : "Firefox",
    "browserVersion" : "latest",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)

def win_edge_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.5.2",
    },
    "browserName" : "Edge",
    "browserVersion" : "latest",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)

def mac_edge_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "OS X",
        "osVersion" : "Big Sur",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.5.2",
    },
    "browserName" : "Edge",
    "browserVersion" : "latest",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)

def mac_safari_session():
    desired_cap = {
    'bstack:options' : {
        "os" : "OS X",
        "osVersion" : "Big Sur",
        "buildName" : build_name,
        "local" : "false",
        "seleniumVersion" : "3.14.0",
    },
    "browserName" : "Safari",
    "browserVersion" : "14.0",
    "browserstack.user" : username,
    "browserstack.key" : access_key
    }
    selenium_assignment.test_case(desired_cap)


t1 = threading.Thread(target=win_chrome_session)
t2 = threading.Thread(target=win_firefox_session)
t3 = threading.Thread(target=win_edge_session)
t4 = threading.Thread(target=mac_chrome_session)
t5 = threading.Thread(target=mac_firefox_session)
t6 = threading.Thread(target=mac_edge_session)
t7 = threading.Thread(target=mac_safari_session)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()