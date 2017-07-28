from common.utils import AUTH_PASSWORD, AUTH_USER
from bok_choy.page_object import PageObject
from pages.sign_in_page import SignInPage


class Homepage(PageObject):
    """
    Studio Homepage
    """
    url = 'https://{}:{}@qa.mckinsey.edx.org/'.format(AUTH_USER,AUTH_PASSWORD)

    def is_browser_on_page(self):
        return self.q(css=".login-btn").visible

    def click_login(self):
        """
        Click on login button and go to the next page
        :return:
        """
        self.q(css=".login-btn").click()
        SignInPage(self.browser).wait_for_page()

