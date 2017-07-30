import unittest

from bok_choy.web_app_test import WebAppTest
from common.utils import NO_OF_MODULES_TO_ATTEMPT
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage


class TestProgress(WebAppTest):
    """
    This class tests the course progress of a student
    """

    def setUp(self):

        super(TestProgress, self).setUp()
        self.homepage = Homepage(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.dashboard = Dashboard(self.browser)

        self.homepage.visit()
        self.homepage.click_login()
        self.sign_in_page.login()
        self.dashboard.select_course()

    def test_progress_persistence(self):
        """

        :return:
        """
        initial_progress = 0

    def test_progress_increase(self):
        """

        :return:
        """

        initial_progress = self.dashboard.get_total_progress()
        total_course_modules = 0
        total_completed_modules = 0

        self.lessons_page.attempt_module(NO_OF_MODULES_TO_ATTEMPT)

        self.dashboard.click_lessons_icon()
        lessons_list = self.dashboard.get_lessons()
        total_lessons = lessons_list.__len__()

        for lesson in lessons_list:

            self.dashboard.go_to_lesson(lessons_list)
            self.lessons_page.click_menu()

            total_modules_of_lesson = self.lessons_page.get_modules()
            completed_modules = self.lessons_page.get_no_of_completed_modules()

            total_course_modules += total_modules_of_lesson
            total_completed_modules += completed_modules

            self.lessons_page.close_module_menu()
            self.lessons_page.click_course_name()

        final_progress = (total_completed_modules/total_course_modules)*100
        displayed_progress = self.dashboard.get_total_progress()

        self.assertEqual(final_progress, displayed_progress)
        self.assertGreater(displayed_progress, initial_progress)





if __name__ == '__main__':
    unittest.main()
