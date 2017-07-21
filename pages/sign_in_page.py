from common.utils import USERNAME, PASSWORD
from bok_choy.page_object import PageObject


class SignInPage(PageObject):
    """
    Sign In page
    """

    url = None

    def is_browser_on_page(self):
        return self.q(css="").visible

    def enter_login_username(self):
        """
        fill username field with user's username
        :return:
        """
        self.q(css="").fill(USERNAME)

    def enter_login_password(self):
        """
        fill password field with password
        :return:
        """
        self.q(css="").fill(PASSWORD)

    def click_login_button(self):
        """
        Click login button
        :return:
        """
        self.q(css="").click()
