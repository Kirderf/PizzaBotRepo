from selenium import webdriver
from time import sleep
class Dominos():
    def __init__(self):
        self.driver = webdriver.Chrome("/home/kirderf/Downloads/chromedriver") #Path to chromedriver

        self.driver.get("http://www.Dominos.no") # Opens website
        sleep(1.0)

    def userData(self):
        self.email = input("Enter a Email: ") 
        self.password = input("Enter password: ")
        self.transport = input("Henting/Levering ? : ")

    def _login(self):
        inputEmail = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div/div/div[2]/form/div[1]/input')
        inputEmail.click()
        inputEmail.send_keys(self.email)

        inputPass = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div/div/div[2]/form/div[2]/input')
        inputPass.click()
        inputPass.send_keys(self.password)

        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div/div/div[2]/form/div[6]').click()

    def order(self):
        newOrder = self.driver.find_element_by_xpath('/html/body/header/nav/div/div[2]/ul/li[2]/a')
        newOrder.click()

        self._login()

        if(self.transport.lower == "henting"):
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/img').click()
        else:
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/img').click()

        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[5]').click()
