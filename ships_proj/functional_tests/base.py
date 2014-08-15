from django.test import TestCase, LiveServerTestCase
from selenium import webdriver

class FunctionalTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # givess FF response time

    def tearDown(self):
        self.browser.quit()

