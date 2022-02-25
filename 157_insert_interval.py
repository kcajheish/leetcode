import unittest

def insert(intervals, newInterval):
    if not intervals:
        return [ newInterval ]
    left, right = [], []
    start, end = newInterval
    for i in intervals:
        if i[1] < start:
            left.append(i)
        elif i[0] > end:
            right.append(i)
        else:
            """
            overlapping between newInterval and interval
            => need merge
            """
            start = min(i[0], start)
            end = max(i[1], end)
    return left + [ [start, end] ] + right


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.insert = insert

    def test_self_contained_new_interval(self):
        intervals = [
            [1,2], [5, 6], [8,9]
        ]
        new_interval = [3,4]
        actual = self.insert(intervals, new_interval)
        expect = [
            [1,2], [3, 4], [5, 6], [8, 9]
        ]
        self.assertEqual(actual, expect)

    def test_overlapping_interval(self):
        intervals = [
            [1,2], [5, 6], [8,9]
        ]
        new_interval1 = [2, 6]
        new_interval2 = [2, 7]
        new_interval3 = [2, 8]
        actual1 = self.insert(intervals, new_interval1)
        actual2 = self.insert(intervals, new_interval2)
        actual3 = self.insert(intervals, new_interval3)
        self.assertEqual(actual1, [ [1, 6], [8, 9] ])
        self.assertEqual(actual2, [ [1, 7], [8, 9] ])
        self.assertEqual(actual3, [ [1, 9] ])


    def test_empty_case(self):
        intervals = []
        new_interval = [1,2]
        actual = self.insert(intervals, new_interval)
        self.assertEqual(actual, [ [1, 2] ])


if __name__ == '__main__':
    unittest.main()
