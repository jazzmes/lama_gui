from selenium import webdriver
import unittest

class InitialProviderAgentListTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_visualization_of_provider_agents_list(self):
        # open homepage
        self.browser.get('http://localhost:8000/monitor')

        # Note: we are unable to test status code using selenium (feature not supported)
        # check title of the page
        self.assertIn('LAMA', self.browser.title)

        # there is an menu option to see all provider agents
        nav = self.browser.find_element_by_tag_name('nav')
        provider_agents_link = nav.find_element_by_link_text('Provider Agents')

        # click the option provider agents
        provider_agents_link.click()
        self.browser.implicitly_wait(3)

        # should see a table with a list of provider agents
        self.assertIn('Provider Agents', self.browser.title)
        providers_table = self.browser.find_element_by_id("providers_table")
        self.assertEqual(providers_table.tag_name, "table")

        # check there is a header with IP and and Id
        headers = providers_table.find_elements_by_xpath("//thead/tr/th")
        ip_index = [h.text for h in headers].index("IP")
        id_index = [h.text for h in headers].index("ID")
        self.assertIsNotNone(ip_index)
        self.assertIsNotNone(id_index)

if __name__ == '__main__':
    unittest.main(warnings='ignore')