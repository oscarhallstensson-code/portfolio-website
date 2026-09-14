import md
import sys, unittest

class MdTests(unittest.TestCase):
    def test_md(self):
        
        self.assertTrue(md.run_md)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())