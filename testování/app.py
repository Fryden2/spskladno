import unittest

class test_obsahuje_jen_písmena(unittest.TestCase):
    def test_jenom_písmena(self):
        self.assertNotIn("1,2,3,4,5,6,7,8,9,0", "mám rád rc kolču moc mi chutná")

suite = unittest.TestLoader().loadTestsFromTestCase(test_obsahuje_jen_písmena)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)