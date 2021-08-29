import create_xml
import unittest
import time
from lxml import etree as et
from selenium import webdriver

data = {
    'browser_type': None,
    'expected_title': None,
    'first_name': None,
    'mail': None,
    'password': None,
    'password_confirm': None
}


def extract_from_xml():
    create_xml.create_xml_file()

    tree = et.parse('config_xml')
    for item in tree.iter():
        tag, text = item.tag, item.text
        if tag in data:
            data[tag] = text


class PageFactory(unittest.TestCase):
    extract_from_xml()
    driver = None

    def __init__(self):
        self.name = data['first_name']
        self.expected_title = data['expected_title']
        self.mail = data['mail']
        self.password = data['password']
        self.confirm_password = data['password_confirm']

    def init_driver(self):
        if data['browser_type'] == 'Chrome':
            self.driver = webdriver.Chrome()
        elif data['browser_type'] == 'Edge':
            self.driver = webdriver.Edge()
        print(data)
        buyme_url = 'https://buyme.co.il/'
        self.driver.get(buyme_url)

    def get_to_website(self):
        self.driver.find_element_by_xpath('//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span').click()
        self.driver.implicitly_wait(1)

    def send_name(self):
        self.driver.find_element_by_css_selector('input[class="ember-view ember-text-field"]').send_keys(
            data['first_name'])
        self.driver.implicitly_wait(1)

    def send_mail(self):
        self.driver.find_element_by_xpath('//*[@id="ember1485"]').send_keys(data['mail'])
        self.driver.implicitly_wait(1)

    def send_password(self):
        self.driver.find_element_by_xpath('//*[@id="valPass"]').send_keys(data['password'])
        self.driver.implicitly_wait(1)

    def send_confirmation_password(self):
        self.driver.find_element_by_xpath('//*[@id="ember1491"]').send_keys(data['password_confirm'])
        self.driver.implicitly_wait(1)

    def click_register(self):
        self.driver.find_element_by_xpath('//*[@id="ember1493"]/span').click()

        if self.driver.find_element_by_xpath('//*[@id="ember1530"]/a/span').text != 'החשבון שלי':
            print('ERROR account didnt create')
        print('Registration test passed successfully')
        time.sleep(5)
