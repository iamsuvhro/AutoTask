# Importing libraries 
from lib2to3.pgen2 import driver
from selenium import webdriver
import datetime
import time


DRIVER_ADDRESS = (
    "chromedriver"
)

class AutoGmeetTask:

    def _getDriver():
        driver = webdriver.Chrome(DRIVER_ADDRESS)
        return driver


    def getlinkOperation(meetingLink: str, leftHours: int):
        """Method to get link for task"""
        # getting the user given details
        meetingLink = meetingLink
        leftHours = leftHours
        res = ()
        # getting the driver
        driver = AutoGmeetTask._getDriver()
        try:
            driver.get(meetingLink)
            driver.maximize_window()
            time.sleep(leftHours * 60)
            button = driver.find_element_by_link_text("Sign In")
            button.click()
        
        except Exception as ex:
            print('Error occur while creating the task')

