from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/files/form.html')

firstNameField = driver.find_element_by_name("firstname")
lastNameField = driver.find_element_by_name("lastname")
sunmitBtn = driver.find_element_by_id("submit")

# 方法一
# firstNameField.send_keys("MRJ")
# lastNameField.send_keys("very good")
# sunmitBtn.click()

# 方法二
action = ActionChains(driver).click(firstNameField).send_keys("xiaojiangjiang").\
    click(lastNameField).send_keys("very nice !").\
    send_keys(Keys.RETURN)
action.perform()

print(driver.find_element_by_tag_name("body").text)

driver.close()