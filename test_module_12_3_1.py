import module_12_3
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        Тестирование метода walk()
        """
        r_obj = module_12_3.Runner('Roman')
        for i in range(10):
            r_obj.walk()
        self.assertEqual(r_obj.distance, 50, 'Метод walk() не прошел проверку')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Тестирование метода run()
        """
        r_obj = module_12_3.Runner('Roman')
        for i in range(10):
            r_obj.run()
        self.assertEqual(r_obj.distance, 100, 'Метод run() не прошел проверку')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        Тестирование методов run() и walk() на неравенство
        """
        r_obj_1 = module_12_3.Runner('Roman')
        r_obj_2 = module_12_3.Runner('Anton')
        for i in range(10):
            r_obj_1.run()
            r_obj_2.walk()
        self.assertNotEqual(r_obj_1.distance,
                            r_obj_2.distance, 'Методы run() и walk() не прошли проверку на неравенство')


if __name__ == '__main__':
    unittest.main()
