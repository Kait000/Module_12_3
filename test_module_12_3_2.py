from module_12_3 import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usein_obj = Runner('Усэйн', 10)
        self.andrey_obj = Runner('Андрей', 9)
        self.nik_obj = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1_usein_and_nik(self):
        """
        Тест метода start для Усэйн(sp=10) и Ник(sp=3)
        """
        self.tour = Tournament(90, self.usein_obj, self.nik_obj)
        x = TournamentTest.all_results[0] = self.tour.start()
        self.assertTrue(Runner(x[max(x)]) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2_andrey_and_nik(self):
        """
        Тест метода start для Андрей(sp=9) и Ник(sp=3)
        """
        self.tour = Tournament(90, self.andrey_obj, self.nik_obj)
        x = TournamentTest.all_results[1] = self.tour.start()
        self.assertTrue(Runner(x[max(x)]) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3_andrey_usein_and_nik(self):
        """
        Тест метода start для Андрей(sp=9), Усэйн(sp=10) и Ник(sp=3)
        """
        self.tour = Tournament(90, self.andrey_obj, self.usein_obj, self.nik_obj)
        x = TournamentTest.all_results[2] = self.tour.start()
        self.assertTrue(Runner(x[max(x)]) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_dop_all(self):
        """
        Доп. тест на короткие дистанции (все пришли к финишу за одну итерацию)
        """
        self.tour = Tournament(5,  self.nik_obj, self.andrey_obj, self.usein_obj)
        x = TournamentTest.all_results[3] = self.tour.start()
        self.assertTrue(Runner(x[max(x)]) == 'Ник')

    @classmethod
    def tearDownClass(cls):
        cls.all_results = dict(sorted(cls.all_results.items()))
        for result, x in cls.all_results.items():
            for a in x:
                x[a] = str(x[a])
            print(x)


if __name__ == '__main__':
    unittest.main()
