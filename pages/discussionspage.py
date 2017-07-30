from bok_choy.page_object import PageObject
from common.utils import TITLE_TEXT, POST_TEXT
from pages.dashboard import Dashboard


class DiscussionsPage(PageObject):

    url = None

    def is_browser_on_page(self):
        return self.q(css=".forum-content").visible

    def add_new_post(self):
        """

        :return:
        """
        self.click_add_post()
        self.add_title()
        self.add_post_text()
        self.click_submit()

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

    def get_discussion_title_text(self):
        """

        :return:
        """
        return self.q(css=".discussion-post>.post-header>.post-header-content>.post-title").text

    def get_discussion_post(self):
        """

        :return:
        """
        return self.q(css="div.post-body>p").text

    def add_search_text(self):
        """

        :return:
        """
        self.q(css=".field-input.input-text.search-input").fill(TITLE_TEXT)

    def click_search_button(self):
        """

        :return:
        """
        self.q(css=".search-btn").click()
        self.wait_for_ajax()

    def get_title_in_search_results(self):
        """

        :return:
        """
        return self.q(css=".forum-nav-thread-title").text

    def click_course_name(self):
        """

        :return:
        """
        self.q(css=".course_info>.course-name>a[href*='/course']").click()
        self.wait_for_ajax()





