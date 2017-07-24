from bok_choy.page_object import PageObject


class ParticipantsPage(PageObject):
    """
    Participants page in admin view
    """

    url = 'https.//{}:{}@qa.mckinsey.edx.org/admin/participants/'.format('mckinsey', 'academy')

    def is_browser_on_page(self):
        return self.q(css="a[href*='/admin/participants']").visible

    def click_add_participant(self):

        self.q(css=".button.participantAddButton").click()
