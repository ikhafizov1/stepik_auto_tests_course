# Исполнение этого кода выведет принт.

#def test_abs1():
#    assert abs(-42) == 42, "Should be absolute value of a number" 

#if __name__ == "__main__":
#    test_abs1()
#    print("All tests passed!")

# Исполнение кода ниже упадет на второй функции и принт не будет выведен.

#def test_abs1():
#    assert abs(-42) == 42, "Should be absolute value of a number"

#def test_abs2():
#    assert abs(-42) == -42, "Should be absolute value of a number"

#if __name__ == "__main__":
#    test_abs1()
#    test_abs2()
#    print("Everything passed")


# Подключаем unitest

#Давайте теперь изменим наши предыдущие тесты, чтобы их можно было запустить с помощью unittest. Для этого нам понадобится выполнить следующие шаги:

#Импортировать unittest в файл: import unittest
#Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
#Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
#Изменить assert на self.assertEqual()
#Заменить строку запуска программы на unittest.main()

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
