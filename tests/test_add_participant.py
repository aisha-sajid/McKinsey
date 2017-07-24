import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.participantspage import ParticipantsPage


class TestAddParticipant(WebAppTest):
    """

    """

    def setUp(self):

        super(TestAddParticipant, self).setUp()
        self.dashboard = Dashboard(self.browser)
        self.participantspage = ParticipantsPage(self.browser)

        self.dashboard.visit()

    def add_participant(self):

        self.dashboard.click_participants()
        self.participantspage.wait_for_page()

        self.participantspage.click_add_participant()



if __name__ == '__main__':
    unittest.main()
