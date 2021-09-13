import random
import sys
import unittest

from lxml import etree as et
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import page_factory
from create_xml import CreateConfig

BROWSER_TYPE = ["Chrome", "Edge"]
NAMES = ["Gabi", "Debi", "Wobi", "Dogie", "Wokie"]

INPUT = {"browser_type": random.choice(BROWSER_TYPE),
         "excepted_title": "BUYME אתר המתנות והחוויות הגדול בישראל |\xa0Gift Card",
         "name": random.choice(NAMES),
         'mail': f"{random.randint(1111111111, 99999999999)}@gmail.com",
         "password": "Abcd1234",
         "password_confirm": "Abcd1234"}


class ByuMeTest(unittest.TestCase):
    driver = None
    page_factory = None
    DATA = dict()

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = ByuMeTest.init_driver()
        cls.page_factory = page_factory.PageFactory(cls.driver)

    @staticmethod
    def init_driver():
        driver = None
        browser = ByuMeTest.DATA['browser_type']
        if browser == 'Chrome':
            driver = webdriver.Chrome()
        elif browser == 'Edge':
            driver = webdriver.Edge()
        buyme_url = 'https://buyme.co.il/'
        driver.get(buyme_url)
        return driver

    def test_registration(self):
        self.page_factory.send_name(ByuMeTest.DATA["name"])
        self.page_factory.send_email(ByuMeTest.DATA["mail"])
        self.page_factory.send_password(ByuMeTest.DATA["password"])
        self.page_factory.send_password_confirmation(ByuMeTest.DATA["password_confirm"])
        self.page_factory.registration()

        try:
            self.driver.find_element_by_id("ember1530")
            flag = True
        except NoSuchElementException:
            flag = False
        self.assertTrue(flag, "Failed to register to BuyMe website")
        self.assertEqual(self.driver.title, ByuMeTest.DATA['excepted_title'])


def create_xml_file():
    config = CreateConfig("buy_me_website")
    for key, val in INPUT.items():
        config.add_child(key, val)
    config.write_to_file("config_xml_for_buy_me.xml")


def extract_data_from_configuration():
    contents_xml_file = et.parse('config_xml_for_buy_me.xml')
    for items in contents_xml_file.iter():
        ByuMeTest.DATA[items.tag] = items.text


def main(out):
    create_xml_file()
    extract_data_from_configuration()
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out).run(suite)


if __name__ == '__main__':
    with open('buy_me_test_result.txt', 'w') as buy_me_test_result:
        main(buy_me_test_result)
