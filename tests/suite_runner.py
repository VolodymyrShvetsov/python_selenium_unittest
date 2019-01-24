import unittest

from tests import tests_1
from tests import tests_2


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(tests_1))
suite.addTests(loader.loadTestsFromModule(tests_2))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
