import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage
from pages.discussionspage import DiscussionsPage
from common.utils import TITLE_TEXT, POST_TEXT


class TestEngagement(WebAppTest):
    """
    This class tests the student's engagement in a course
    """

    def setUp(self):
        """

        :return:
        """
        super(TestEngagement, self).setUp()
        self.homepage = Homepage(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.dashboard = Dashboard(self.browser)
        self.discussion_page = DiscussionsPage(self.browser)

        self.homepage.visit()
        self.homepage.click_login()
        self.sign_in_page.login()
        self.dashboard.select_course()

    def test_engagement_increase(self):
        """

        :return:
        """
        initial_engagement = self.dashboard.get_total_engagement()

        self.dashboard.click_discussion_icon()
        self.discussion_page.click_add_post()
        self.discussion_page.add_new_post()
        self.discussion_page.click_course_name()

        final_engagement = self.dashboard.get_total_engagement()

        self.assertEqual(initial_engagement+10, final_engagement)


if __name__ == '__main__':
    unittest.main()



