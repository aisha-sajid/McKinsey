import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.participants_page import ParticipantsPage


class TestAddParticipant(WebAppTest):
    """

    """

    def setUp(self):

        super(TestAddParticipant, self).setUp()
        self.dashboard = Dashboard(self.browser)