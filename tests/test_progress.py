import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage


class TestProgress(WebAppTest):
    """
    This class tests the course progress of a student
    """

    def setUp(self):

        super(TestProgress, self).setUp()
        self.homepage = Homepage(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.dashboard = Dashboard(self.browser)

        self.homepage.visit()
        self.homepage.click_login()
        self.sign_in_page.login()


    def test_progress_persistence(self):
        """

        :return:
        """
        initial_progress = 0

    def test_progress_increase(self):
        """

        :return:
        """

        initial_progress = self.dashboard.get_total_progress()
        print self.dashboard.get_lessons()



if __name__ == '__main__':
    unittest.main()
