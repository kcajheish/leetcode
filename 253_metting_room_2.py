import unittest

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval start: {self.start}, end: {self.end}"

    def __lt__(self, other):
        return self.end < other.end

def min_metting_room(intervals):
    rooms = []
    for interval in sorted(intervals, key=lambda i: i.start):
        has_book = False
        for room in rooms:
            if interval.start > room[-1].end:
                room.append(interval)
                has_book = True
                break
        if not has_book:
            rooms.append([interval])
    return len(rooms)

class TestMinMettingRoom(unittest.TestCase):
    def setUp(self):
        self.min_room = min_metting_room

    def test_min_metting_room(self):
        self.assertEqual(0, self.min_room([]))
        self.assertEqual(1, self.min_room([Interval(0, 1)]))
        self.assertEqual(2, self.min_room([ Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(1, self.min_room([Interval(7, 10), Interval(2, 4)]))

from heapq import heappush, heappop
def min_meeting_room(intervals):
    rooms = [Interval(float('inf', 'inf'))]
    for interval in intervals:
        if interval.start >= rooms[0].end:
            heappop(rooms)
            heappush(rooms, interval)
        else:
            heappush(rooms, interval)
    return len(rooms)


class TestHeapMettingRoom(unittest.TestCase):
    def setUp(self):
        self.min_room = min_metting_room

    def test_min_metting_room(self):
        self.assertEqual(0, self.min_room([]))
        self.assertEqual(1, self.min_room([Interval(0, 1)]))
        self.assertEqual(2, self.min_room([ Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(1, self.min_room([Interval(7, 10), Interval(2, 4)]))


if __name__ == '__main__':
    unittest.main()