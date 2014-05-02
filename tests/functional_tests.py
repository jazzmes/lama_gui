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
        self.browser.get('http://localhost:8000')

        # Note: we are unable to test status code using selenium (feature not supported)
        # check title of the page
        self.assertIn('LAMA', self.browser.title)

        # there is an menu option to see all provider agents
        nav = self.browser.find_element_by_tag_name('nav')
        self.assertIsNotNone(nav)
        provider_agents_link = nav.find_element_by_xpath('ul/li[text()="Provider Agents"]')
        self.assertIsNotNone(provider_agents_link)

        # click the option provider agents
        # should see a table with a list of provider agents

        # each line should contains id and ip address of the agent
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')