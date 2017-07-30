import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage
from pages.discussionspage import DiscussionsPage
from common.utils import TITLE_TEXT, POST_TEXT


class TestDiscussion(WebAppTest):
    """
    This class tests the discussions page
    """

    def setUp(self):
        """

        :return:
        """
        super(TestDiscussion, self).setUp()
        self.homepage = Homepage(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.dashboard = Dashboard(self.browser)
        self.discussion_page = DiscussionsPage(self.browser)

        self.homepage.visit()
        self.homepage.click_login()
        self.sign_in_page.login()
        self.dashboard.select_course()

    def test_add_post(self):
        """

        :return:
        """
        self.dashboard.click_discussion_icon()
        self.discussion_page.click_add_post()
        self.discussion_page.add_new_post()

        assert TITLE_TEXT in self.discussion_page.get_discussion_title_text()
        assert POST_TEXT in self.discussion_page.get_discussion_post_text()

    def test_search_post(self):
        """

        :return:
        """
        self.dashboard.click_discussion_icon()
        self.discussion_page.add_search_text()
        self.discussion_page.click_search_button()

        assert TITLE_TEXT in self.discussion_page.get_title_in_search_results()










