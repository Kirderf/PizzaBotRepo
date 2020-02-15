from selenium import webdriver
from time import sleep

"""
Requirements:
Python3
Selenium
Chromedriver(for Chrome browser)

"""

class Pizzabakeren():
    def __init__(self):
        self.driver = webdriver.Chrome("/home/kirderf/Downloads/chromedriver") #Path to chromedriver

        self.driver.get("http://www.pizzabakeren.no") # Opens website
        sleep(1.0)



    def  getUserData(self):
        self.pizzaNr = input("Input pizza number :")
        self.isUser = "True" == input("Are you a pizzabakeren user ? True/False :")
        print(self.isUser)
        if self.isUser:
            self.username = input("Username (Phone number) :")
            self.password = input("Password :")
            self._login()
        else:
            self.name = input("Input name :")
            self.email = input("Input email :")
            self.phoneNr = input("Input phone number :")

    def _getPizzaVariant(self,goal):
        return {
            '1': 8,
            '2': 26,
            '3': 25,
            '4': 24,
            '5': 23,
            '6': 22,
            '7': 12,
            '8': 21,
            '9': 20,
            '10': 19,
            '11': 18,
            '12': 61,
            '13': 11,
            '14': 27,
            '16': 10,
            '17': 9,
            '18': 7,
            '19': 200,
            '20': 16,
            '21': 15,
            '22': 184,
            '23': 13,
            '24': 178,
            '25': 182,
            '26': 128,
            '27': 136,
            '28': 137,
            '29': 239,
            '30': 247,
            '31': 299,
            '32': 338,

        }.get(goal,8)







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
        if not (self.isUser):
            self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div[2]/div[1]/a[1]').click()
        
        #Select the menu
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div[2]/div[1]/ul/div[1]/div[1]/li/a').click()

        #Closes the cookies
        if (self.isUser):
            self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[9]/button').click()
        else:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[8]/button').click()
        #Selecting the pizza
        self.driver.find_element_by_xpath("//a[contains(@onclick,'pvariant" + str(self._getPizzaVariant(self.pizzaNr)) +"')]").click()
        sleep(1.0)


        if not (self.isUser):
            self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/form/div/a[3]').click()
            
    def storeSelect(self):
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
        print("Store found")
        #Selecting to pickup order
        self.driver.find_element_by_xpath('//*[@id="radio-1"]').click()
        #Exiting store select tab
        self.driver.find_element_by_xpath('//*[@id="psSearchResults"]/div[3]/a').click()
        print("Done store selecting")

    def preCheckoutUser(self):
        print("Starting pre-checkout")
        #Selecting checkout
        self.driver.find_element_by_xpath('//*[@id="mini_cart"]/div[3]/a[2]').click()
        #Selecting payment method (card)
        self.driver.find_element_by_xpath('//*[@id="payment-1"]').click()
        #exiting pre-payment window
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div[2]/div[1]/form/div[2]/button[2]').click()
        print("Finished pre-checkout")

    def preCheckout(self):
        print("Starting pre-checkout")
        #Opening cart
        self.driver.find_element_by_xpath('//*[@id="cartBox"]/div[1]/a/span[2]').click()
        sleep(1)
        #Selecting checkout
        self.driver.find_element_by_xpath('//*[@id="mini_cart"]/div[3]/a[2]').click()

        #Fillig out form
        formName = self.driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/div[1]/form/div[1]/div[1]/input')
        formName.click()
        formName.send_keys(self.name)

        formPhonenumber = self.driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/div[1]/form/div[1]/div[2]/input')
        formPhonenumber.click()
        formPhonenumber.send_keys(self.phoneNr)

        formEmail = self.driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/div[1]/form/div[1]/div[3]/input')
        formEmail.click()
        formEmail.send_keys(self.email)



        #exiting pre-payment window
        self.driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/div[1]/form/div[2]/button').click()
        print("Finished pre-checkout")

bot = Pizzabakeren()
bot.getUserData()

if bot.isUser:
    bot.storeSelect()
    bot.order()
    bot.preCheckoutUser()
else:
    bot.order()
    bot.storeSelect()
    bot.preCheckout()

