import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.participantspage import ParticipantsPage


class TestProgress(WebAppTest):
    """
    This class tests the course progress of a student
    """

    def setUp(self):

        super(TestProgress, self).setUp()
        self.dashboard = Dashboard(self.browser)
        self.participantspage = ParticipantsPage(self.browser)

        self.dashboard.visit()
        self.dashboard.click_admin()

    def test_progress_persistence(self):
        """

        :return:
        """
        initial_progress = 0

    def test_progress_increase(self):
        """
        
        :return:
        """