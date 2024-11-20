import unittest
import test_module_12_3_1
import test_module_12_3_2


testST = unittest.TestSuite()
testST.addTest((unittest.TestLoader().loadTestsFromTestCase(test_module_12_3_1.RunnerTest)))
testST.addTest((unittest.TestLoader().loadTestsFromTestCase(test_module_12_3_2.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
