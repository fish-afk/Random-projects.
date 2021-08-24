from selenium import webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe', options=options)


class Driver:

    def __init__(self):
        super().__init__()

        self.URL = "https://www.instagram.com"
        self.wait = 3.2345
        self.wait2 = 2.0

    def url_getter(self):
        driver.get(self.URL)

    def implicit_wait(self):
        driver.implicitly_wait(self.wait)

    def implicit_wait_2(self):
        
        driver.implicitly_wait(self.wait2)


