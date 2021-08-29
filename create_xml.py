from lxml import etree as Et

INPUT = {"browser_type": "Chrome", "excepted_title": "title_to_insert", "first_name": "Gabi",
         'mail': "gabikakakaka@gmail.com", "password": "Gabi1994@gmail.com", "password_confirm": "Gabi1994@gmail.com"}


class CreateConfig:

    def __init__(self, root_name):
        self.__root = Et.Element(root_name)
        self.__tree = Et.ElementTree(self.__root)

    def add_child(self, tag_name, text):
        Et.SubElement(self.__root, tag_name).text = text

    def write_to_file(self, file_name):
        self.__tree.write(file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')


def create_xml_file():
    config = CreateConfig("buy_me_website")
    for key, value in INPUT.items():
        config.add_child(key, INPUT[key])
    config.write_to_file("config_xml")
