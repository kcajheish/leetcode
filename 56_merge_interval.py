import unittest

def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda interval: interval[0])
    merge_list = []
    for interval in intervals:
        if not merge_list:
            merge_list.append(interval)
            continue

        if interval[0] > merge_list[-1][1]:
            merge_list.append(interval)
        else:
            merge_item = merge_list[-1]
            merge_list[-1]= [
                max(interval[1], merge_item[1])
            ]

    return merge_list


class TestMergeInterval(unittest.TestCase):
    def setUp(self):
        self.merge = merge

    def test_two_interval_overlapping(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        merge_interval = self.merge(intervals)
        self.assertEqual(merge_interval, [ [1,6], [8, 10], [15, 18] ])

        intervals = [[1,4],[4,5]]
        expect = [[1,5]]
        actual = self.merge(intervals)
        self.assertEqual(actual, expect)

    def test_empty(self):
        expect = []
        actual = self.merge([])
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
