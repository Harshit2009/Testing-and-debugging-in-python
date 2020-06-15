import unittest
import bubblesort as st

class Test_TestValue(unittest.TestCase):
    def test_simple(self):
        testList = [4,3,2,1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubblesort(testList)
        self.assertEqual(actualList, expectedList)      