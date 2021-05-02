# This project uses Selenium along with the headless browser PhantomJS to check if you've been admitted to a specific program at the University of Waterloo!
# It also uses time just to account for wifi and page loading ^_^
import time
from selenium import webdriver

# Enter your login details here ****************************
username = ""
password = ""

# Creates a driver
driver = webdriver.PhantomJS()

# URL to the quest login
url = "https://adfs.uwaterloo.ca/adfs/ls/idpinitiatedsignon.aspx?LoginToRP=urn:quest.ss.apps.uwaterloo.ca"

# Directs the browser to the Quest login
driver.get(url)

# Signs in using username and password
driver.find_element_by_id("userNameInput").send_keys(username)
driver.find_element_by_id("nextButton").click()
driver.find_element_by_id("passwordInput").send_keys(password)
driver.find_element_by_id("submitButton").click()

# Clicks on the admissions tab
driver.find_element_by_id("win0groupletPTNUI_LAND_REC_GROUPLET$0").click()

# This stops the code for 4 seconds allowing time for the page to load
time.sleep(4)

# The code switches to the main iFrame
driver.switch_to.frame(driver.find_element_by_id("main_target_win0"))

#Enter the name of the program you'd like to check as it shows on the admissions page on Quest ****************************
driver.find_element_by_link_text("Computer Science, Honours, Co-operative Program").click()

# This stops the code for 4 seconds allowing time for the page to load
time.sleep(4)

# The code switches to the main iFrame
driver.switch_to.frame(driver.find_element_by_id("ptifrmtgtframe"))

# Just a line

print()

# Checks whether you've been admitted or not!!

if driver.find_element_by_id("STATUS$0").text == "Application":
    print("Not Admitted")
else:
    print("YOU GOT ADMITTED!!! YOU ARE IIINNNNNNNN")

# Just a line

print()
