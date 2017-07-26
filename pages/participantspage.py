from bok_choy.page_object import PageObject
from common.utils import AUTH_PASSWORD, AUTH_USER
from common.utils import FIRST_NAME, LAST_NAME, USER_EMAIL, COMPANY, COURSE_ID


class ParticipantsPage(PageObject):
    """
    Participants page in admin view
    """

    url = 'https.//{}:{}@qa.mckinsey.edx.org/admin/participants/'.format(AUTH_USER ,AUTH_PASSWORD)

    def is_browser_on_page(self):
        return self.q(css="a[href*='/admin/participants']").visible

    def click_add_participant(self):

        self.q(css=".button.participantAddButton").click()
        self.wait_for_ajax()

    def fill_participant_form(self):

        self.q(css=".participantFirstNameValue").fill(FIRST_NAME)
        self.q(css=".participantLastNameValue").fill(LAST_NAME)
        self.q(css=".participantEmailValue").fill(USER_EMAIL)
        self.q(css=".participantCompanyValue").fill(COMPANY)

        self.q(css=".addAnotherCourseWrapper>.large-12").click()
        self.wait_for_ajax()
        self.q(css=".participantCourseValue>.ui-autocomplete-input").fill(COURSE_ID)

        self.q(css=".emailActivationCheckbox").click()
        self.q(css=".button.addSingleParticipantButton").click()

    def get_success_message(self):
        """

        :return:
        """

        upload_message = self.q(css= ".upload_message").text

        return upload_message






