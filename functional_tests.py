import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_page(self):
        self.browser.get('http://127.0.0.1:8000')

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bridging Coursework', header_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')