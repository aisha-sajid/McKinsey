from bok_choy.page_object import PageObject
from common.utils import TITLE_TEXT, POST_TEXT
from pages.dashboard import Dashboard


class DiscussionsPage(PageObject):

    url = None

    def is_browser_on_page(self):
        return self.q(css=".forum-content").visible

    def click_add_post(self):
        """

        :return:
        """
        self.q(css=".new-post-btn").click()
        self.wait_for_ajax()

    def add_title(self):
        """

        :return:
        """
        self.q(css=".js-post-title.field-input").fill(TITLE_TEXT)

    def add_post_text(self):
        """

        :return:
        """
        self.q(css=".wmd-input").fill(POST_TEXT)

    def click_submit(self):
        """

        :return:
        """
        self.q(css=".btn-brand.submit").click()
        self.wait_for_ajax()

    def click_cancel_button(self):
        """

        :return:
        """
        self.q(css=".btn.cancel").click()
        self.wait_for_ajax()

    def search_post(self):
        """

        :return:
        """



