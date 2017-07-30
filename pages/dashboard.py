from common.utils import AUTH_PASSWORD, AUTH_USER
from bok_choy.page_object import PageObject
from pages.participantspage import ParticipantsPage
from pages.discussionspage import DiscussionsPage
from pages.lessons_page import LessonsPage


class Dashboard(PageObject):

    url = None

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

    def select_course(self):
        """

        :return:
        """
        self.q(css=".course-name").click()
        self.q(css=".course-name").nth()

    def get_total_progress(self):
        """

        :return:
        """
        total_progress = self.q(css=".course-progress>.visualization>.total").text

        return total_progress

    def is_course_complete(self):
        """

        :return:
        """
        course_status = self.q(css=".lesson-progress").text

        if course_status != "Completed":
            return 0
        else:
            return 1

    def click_discussion_icon(self):
        """

        :return:
        """
        self.q(css="a[href*='/discussion']").click()
        DiscussionsPage(self.browser).wait_for_page()

    def get_total_engagement(self):
        """

        :return:
        """
        return self.q(css=".course-engagement>.visualization>.total").text

    def click_lessons_icon(self):
        """

        :return:
        """
        self.q(css="ul.course-tabs>li>a.nav-1[href*='/lesson']").click()

    def get_lessons(self):
        """

        :return:
        """
        lessons_list = self.q(css=".lesson-row-item>.lesson-item-name>a")
        return lessons_list

    def go_to_lesson(self, lesson):
        """

        :return:
        """
        lesson.click()
        LessonsPage(self.browser).wait_for_page()


