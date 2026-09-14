import sys, unittest
from ase.lattice.cubic import FaceCenteredCubic
from md import calcenergy
from asap3 import EMT


class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        atoms = FaceCenteredCubic(
            directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            symbol='Cu',
            size=(10, 10, 10),
            pbc=True,
            )
        atoms.calc = EMT()
        self.assertEqual(len(calcenergy(atoms)), 4)


if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())