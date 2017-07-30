from bok_choy.page_object import PageObject
from pages.dashboard import Dashboard


class LessonsPage(PageObject):
    """

    """
    url = None

    def is_browser_on_page(self):
        return self.q(css=".lesson-content").visible

    def click_menu(self):
        """

        :return:
        """
        self.q(css="a>.fa.fa-list-ul").click()
        self.wait_for_ajax()

    def get_modules(self):
        """

        :return:
        """
        total_modules = self.q(css="div.lesson-modules-modal>ul>li.lesson-row-item").__len__()
        return total_modules

    def get_no_of_completed_modules(self):
        """

        :return:
        """
        completed_modules = self.q(css=".fa-check-circle:not(.complete)").__len__()
        return completed_modules

    def close_module_menu(self):
        """

        :return:
        """
        self.q(css=".close-reveal-modal>.fa-times-circle").click()
        self.wait_for_ajax()

    def click_course_name(self):
        """

        :return:
        """
        self.q(css=".course-name>a[href*='/course']").click()
        Dashboard(self.browser).wait_for_page()

    def attempt_module(self, no_of_modules_to_attempt):
        """

        :param no_of_modules_to_attempt:
        :return:
        """

    