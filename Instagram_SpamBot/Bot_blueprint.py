import time
from driver_init import Driver, driver
from colorama import *
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

our_driver = Driver()


class Auto_Spam_Bot:

    def __init__(self, username, password):
        super().__init__()

        self.username = username
        self.password = password
        self.xpath_for_not_now_btns = '//button[normalize-space()="Not Now"]'
        self.xpath_for_dm_btn = '//div[@class="XrOey"]/a'
        self.time_sleep = 2

        self.unexpected_error = Fore.RED + "Unexpected error occurred..." + Fore.RESET
        self.spam_text_file = "spam_text.txt"
        self.time_sleep_2 = 0.527366264928348927348273472834729837489273  # messing around
        self.range = 2

    def login_with_these(self):

        our_driver.url_getter()
        our_driver.implicit_wait()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").send_keys(self.username)

        time.sleep(1)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(self.password)

        our_driver.implicit_wait_2()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def say_no_to_save_info(self):

        time.sleep(self.time_sleep)
        driver.find_element_by_xpath(self.xpath_for_not_now_btns).click()
        driver.find_element_by_xpath(self.xpath_for_not_now_btns).click()

    def click_on_the_dms(self):

        our_driver.implicit_wait_2()
        print(Fore.RED + "-->[ENTERING DMs....]" + Fore.RESET)

        try:

            driver.find_element_by_xpath(self.xpath_for_dm_btn).click()
            print(Fore.GREEN + "Entered Dm section successfully \u2713 \n" + Fore.RESET)

        except WebDriverException:

            print("Unexpected error occcurred while trying to enter Dm section...")

    def enter_first_chat_from_dms(self):

        try:

            print(Fore.GREEN + "Entered First Dm... \u2713" + Fore.RESET)
            driver.find_element_by_xpath('//a[@class="-qQT3 rOtsg"]').click()
            time.sleep(self.time_sleep)

        except WebDriverException:

            print(self.unexpected_error)

    def start_spam_procedure(self):

        with open(self.spam_text_file, "r") as file:
            spam_text = file.readline()

        try:
            print(Fore.RED + "\n[Initiating spamming session....]" + Fore.RESET)

            for attempt in range(1, self.range+1, +1):

                if attempt == 25:
                    time.sleep(0.3)
                else:
                    driver.find_element_by_tag_name("textarea").click()
                    driver.find_element_by_tag_name("textarea").send_keys(spam_text)
                    driver.find_element_by_tag_name("textarea").send_keys(Keys.ENTER)
                    time.sleep(self.time_sleep_2)

                if attempt == self.range:
                    print(Fore.GREEN + "Spamming session was successful... \u2713" + Fore.RESET)

        except:
            print(self.unexpected_error)




