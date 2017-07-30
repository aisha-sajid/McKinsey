import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage

class TestLesson(WebAppTest):
    """

    """

    def setUp(self):
        """

        :return:
        """
        super(TestLesson, self).setUp()
        self.homepage = Homepage(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.dashboard = Dashboard(self.browser)

        self.homepage.visit()
        self.homepage.click_login()
        self.sign_in_page.login()
        self.dashboard.select_course()


