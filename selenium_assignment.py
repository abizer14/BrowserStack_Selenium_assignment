from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_case(desired_cap):

    driver = webdriver.Remote("https://hub-cloud.browserstack.com/wd/hub", desired_cap)

    driver.implicitly_wait(15)
    driver.maximize_window()

    #Open URL
    driver.get("https://flipkart.com")

    #Close the Flipkart account login popup
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

    #Search for Samsung Galaxy S10
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys("Samsung Galaxy S10")
    search_bar.submit()
    time.sleep(2)

    #Filter by Samsung Brand
    samsung_brand = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[6]/div[2]/div/div/div/label/div[1]')
    driver.execute_script("arguments[0].scrollIntoView();", samsung_brand)
    driver.execute_script("arguments[0].click()", samsung_brand)
    time.sleep(2)

    #Filter by Flipkart Assured
    driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[3]/label/div[1]').click()
    time.sleep(2)

    #Sort by price: High to low
    driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[4]').click()

    #fetching and printing product name, price and product link
    results = driver.find_elements_by_class_name("_13oc-S")

    for result in results:
        print("--------------------------------------------")
        print("Product Name: " + result.find_element_by_class_name("_4rR01T").text)
        print("Price: " + result.find_element_by_css_selector("div._30jeq3._1_WHN1").text)
        print("Link to product: " + result.find_element_by_class_name("_1fQZEK").get_attribute("href"))
        print("\n\n")
        time.sleep(2)

    driver.quit()