# Тестраннер зайдет в этот класс, т.е. наименование класса начинается на Test
class TestLessonCreate():
    # номер 5 тест будет запущен раннером т.к. наименование ф-ции начинается на test
    def test_create_lesson(self, browser):
        pass
    # номер 6 тест не будет запущен, некорректное наименование ф-ции
    def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):
        pass
# Тестраннер не зайдет в этот класс, некорректное наименование
class CourseCreate():
    # номер 7 следовательно не будет выполнен несмотря на корректное наименование
    def test_create_course(self, browser):
        pass
# номер 8 тест будет запущен, т.к. функция находится вне класса с корректным наименованием.
def test_guest_can_open_new_course(browser):
    pass


=============================================== short test summary info ===============================================
ERROR test_project/test_regression.py::TestLessonCreate::test_create_lesson
ERROR test_project/test_regression.py::test_guest_can_open_new_course
================================================== 2 errors in 0.03s ===
