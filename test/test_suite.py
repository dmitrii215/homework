import unittest
from учеба.test import test_new_calc

calcST = unittest.TestSuite()
# calcST.addTest(unittest.makeSuite(test_calc.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calkST)