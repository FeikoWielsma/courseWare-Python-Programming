import unittest

class ReverseTests(unittest.TestCase):
    def setUp(self):
        from listfunctions import reverse
        self.reverse = reverse
        self.aList = [1, 2, 3]
        
    def tearDown(self):
        del self.aList
    
    def test_normal(self):
        self.assertEqual(self.reverse([1, 2, 3]), [3, 2, 1])
        
    def test_doesntMutate(self):
        #self.assertEqual(self.reverse(self.aList), [3, 2, 1])
        self.assertEqual(self.aList, [1, 2, 4])