import page_factory


class TestBuyMe:
    page_factory = page_factory.PageFactory()
    page_factory.init_driver()
    page_factory.get_to_website()

    def __init__(self):
        self.driver = self.page_factory.driver

    def test_registration(self):
        self.page_factory.send_name()
        self.page_factory.send_mail()
        self.page_factory.send_password()
        self.page_factory.send_confirmation_password()
        self.page_factory.click_register()

    def test_title(self):
        if self.page_factory.driver.title != page_factory.data['expected_title']:
            print('ERROR failed test_title')
            return
        print('test_register completed successfully')


x = TestBuyMe()
x.test_title()
x.test_registration()
