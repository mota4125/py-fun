import unittest

# Discover and run all test files under the "tests" directory
loader = unittest.TestLoader()
suite = loader.discover(start_dir="tests", pattern="test_*.py")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
