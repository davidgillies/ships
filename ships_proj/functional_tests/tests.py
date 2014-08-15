from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


class NewVisitorTest(FunctionalTest):

    def test_ships_in_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Ships', self.browser.title)   

#    def test_for_list_of_ships(self):
#        self.browser.get(self.live_server_url)
#        ship_list = self.browser.find_elements_by_class_name('ship')
#        self.assertTrue(len(ship_list)>0)

#    def test_ship_links_work(self):
#        self.browser.get(self.live_server_url)
#        ship_list = self.browser.find_elements_by_class_name('ship')
#       for ship in ship_list:
#             status = requests.get(ship.get_attribute('href')).status_code
#             self.assertTrue(status == 200, msg="%s, %s"%(link.text, status)) 
