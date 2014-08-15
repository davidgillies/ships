from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

class NewVisitorTest(FunctionalTest):
    
    def test_ships_in_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Ships', self.browser.title)   

 
