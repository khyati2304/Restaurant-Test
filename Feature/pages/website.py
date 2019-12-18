from framework.webapp import webapp


class website():
    instance = None
    rest = None
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = website()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def search_pincode(self, pin):
        print('coming here...')
        rest=self.driver.find_element(self, pin)

    def verify_rest(self):
        print('coming here. restaurants..')
        if self.rest is None:
            print("Failed")
        else:
            print("success")

    def search_discount_rest(self):
        print('all restaurants..')
        if self.rest is None:
            print("Failed")
        else:
            print("success")

website = website.get_instance()