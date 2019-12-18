from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin


class website:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = website()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings[' http://www.just-eat.co.uk/'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings[' http://www.just-eat.co.uk/'], page.lower()))

website = website.get_instance()
