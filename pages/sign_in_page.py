from common.utils import USERNAME, PASSWORD
from bok_choy.page_object import PageObject
from pages.dashboard import Dashboard


class SignInPage(PageObject):
    """
    Sign In page
    """

    url = None

    def is_browser_on_page(self):
        return self.q(css=".normal-login>#id_username").visible

    def enter_login_username(self):
        """
        fill username field with user's username
        :return:
        """
        self.q(css=".normal-login>#id_username").fill(USERNAME)

    def enter_login_password(self):
        """
        fill password field with password
        :return:
        """
        self.q(css=".normal-login>#id_password").fill(PASSWORD)

    def click_login_button(self):
        """
        Click login button
        :return:
        """
        self.q(css=".button").click()
        Dashboard(self.browser).wait_for_page()

    def login(self):
        """
        login a user
        """

        self.enter_login_email()
        self.enter_login_password()
        self.click_sign_in_button()
