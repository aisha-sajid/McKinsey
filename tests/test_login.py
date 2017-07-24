import unittest

from bok_choy.web_app_test import WebAppTest
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage
from pages.dashboard import Dashboard


class TestLogin(WebAppTest):
    """
    Test Studio Site
    """

    def setUp(self):
        """
        This function instantiates the PageObject
        :return: none
        """

        super(TestLogin, self).setUp()
        self.homepage = Homepage(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.dashboard = Dashboard(self.browser)

        self.homepage.visit()
        self.homepage.sign_in()

    def click_sign_in_homepage(self):
        """
        Click Sign in button on McKinsey Homepage
        :return:
        """

        self.homepage.click_login()

    def login(self):
        """
        login the user to studio
        :return:
        """

        self.sign_in_page.login()


if __name__ == '__main__':
    unittest.main()

