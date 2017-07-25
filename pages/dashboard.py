from bok_choy.page_object import PageObject
from pages.participantspage import ParticipantsPage


class Dashboard(PageObject):

    url = 'https.//{}:{}@qa.mckinsey.edx.org/admin/'.format('mckinsey', 'academy')

    def is_browser_on_page(self):
        return self.q(css="a[href*='/admin']").visible

    def click_admin(self):
        """
        Click the admin button in the top menubar
        :return:
        """
        self.q(css="a[href*='/admin']").click()

    def click_participants(self):
        """
        Click the participants button on the top menu of admin dashboard
        :return:
        """
        self.q(css="a[href*='/admin/participants']").click()
        ParticipantsPage(self.browser).wait_for_page()


