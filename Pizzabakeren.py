from selenium import webdriver
from time import sleep

"""
Requirements:
Python3
Selenium
Chromedriver(for Chrome browser)

"""

class Pizzabaker():
    def __init__(self):
        self.driver = webdriver.Chrome("/home/kirderf/Downloads/chromedriver") #Path to chromedriver

        self.driver.get("http://www.pizzabakeren.no") # Opens website
        sleep(1.0)



    def  getUserData(self):
        self.pizzaNr = input("Input pizza number :")
        self.isUser = input("Are you a pizzabakeren user ? True/False :")

        if self.isUser:
            self.username = input("Username (Phone Number) :")
            self.password = input("Password :")


    def _login(self):
         #Logging in to pizzabakeren userdb
            self.driver.get("https://www.pizzabakeren.no/box_login.php")
            print("Logging in")
            sleep(1.0)
            #Selecting PhoneNumber slot
            loginPhoneNr = self.driver.find_element_by_xpath('/html/body/div[1]/div/form/input[1]')
            loginPhoneNr.click()
            #Sending keys(Phone Number) to website
            loginPhoneNr.send_keys(self.username)
            #Selecting password slot
            loginPass = self.driver.find_element_by_xpath('/html/body/div[1]/div/form/input[2]')
            loginPass.click()
            #Sending keys(Password) to website
            loginPass.send_keys(self.password)
            #Selecting Login button and clicking it
            self.driver.find_element_by_xpath('/html/body/div[1]/div/form/button').click()
            print("Login complete")
            sleep(0.5)



    def order(self):
        
        #Make A Pizza order
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div[2]/div[1]/a[1]').click()
        
        #Select the menu
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div[2]/div[1]/ul/div[1]/div[1]/li/a').click()

        #Closes the cookies
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[8]/button').click()

        #Selecting the pizza
        self.driver.find_element_by_xpath("//a[contains(@onclick,'pvariant" + self.pizzaNr +"')]").click()
        sleep(1.0)


        if(self.isUser):
           self._login()


        #Clearing the store slot
        print("Selecting Store")
        self.driver.find_element_by_xpath('//*[@id="modal_search"]/div[1]/span').click()
        #Searching for stores
        storeSearch = self.driver.find_element_by_xpath('//*[@id="psSearchInput"]')
        #Sending keys(Store name) to website
        storeSearch.send_keys('Trondheim')
        sleep(2.5)
        #Selecting store found
        self.driver.find_element_by_xpath('//*[@id="bestil-470"]').click()

        #Selecting to pickup order
        self.driver.find_element_by_xpath('//*[@id="radio-1"]').click()
        #Exiting store select tab
        self.driver.find_element_by_xpath('//*[@id="psSearchResults"]/div[3]/a').click()
        
        #Opening cart
        self.driver.find_element_by_xpath('//*[@id="cartBox"]/div[1]/a/span[2]').click()
        sleep(1)
        #Selecting checkout
        self.driver.find_element_by_xpath('//*[@id="mini_cart"]/div[3]/a[2]').click()
        #Selecting payment method (card)
        self.driver.find_element_by_xpath('//*[@id="payment-1"]').click()
        #exiting pre-payment window
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div[2]/div[1]/form/div[2]/button[2]').click()


bot = Pizzabaker()
bot.getUserData()
bot.order()

