import unittest

from bok_choy.web_app_test import WebAppTest
from pages.dashboard import Dashboard
from pages.participantspage import ParticipantsPage


class TestAddParticipant(WebAppTest):
    """
    This test adds a new participant
    """

    def setUp(self):

        super(TestAddParticipant, self).setUp()
        self.dashboard = Dashboard(self.browser)
        self.participantspage = ParticipantsPage(self.browser)

        self.dashboard.visit()

    def test_add_participant(self):

        self.dashboard.click_participants()
        self.participantspage.wait_for_page()

        self.participantspage.click_add_participant()
        self.participantspage.fill_participant_form()

        success_message = self.participantspage.get_success_message()

        self.assertEqual(success_message, "Successfully added new user!")


if __name__ == '__main__':
    unittest.main()
