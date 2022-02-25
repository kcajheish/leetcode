import unittest

def canAttendMettings(intervals):
    last = [float('-inf'), float('-inf')]
    for i in sorted(intervals):
        if i[0] < last[1]:
            return False
        last = i
    return True

class TestAttendMettings(unittest.TestCase):
    def setUp(self):
        self.can_attend = canAttendMettings

    def test_can_attend_all(self):
        intervals = [[1,2], [3,4], [6,7]]
        self.assertTrue(self.can_attend(intervals))

    def test_cannot_attend_all(self):
        intervals = [[1,3], [2, 4]]
        self.assertFalse(self.can_attend(intervals))

        intervals = [ [0, 30], [5, 10], [15, 20] ]
        self.assertFalse(self.can_attend(intervals))

if __name__ == '__main__':
    unittest.main()