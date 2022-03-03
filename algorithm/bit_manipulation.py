
"""
one bit at position k, using left shift: 1 << k
kth bit of a number, n: check n & (1 << k)
"""
def to_binary(n):
    results = []
    num_of_digits = 32
    for i in range(num_of_digits, -1, -1):
        results.append(str(n >> i & 1))
    return ''.join(results)

def to_binary_v2(n):
    results = []
    num_of_digits = 32
    for i in range(num_of_digits, -1, -1):
        if (n & (1 << i)):
            results.append('1')
        else:
            results.append('0')
    return ''.join(results)

def set_kth_bit_to_one(n, k):
    return n | (1 << k)

def set_kth_bit_to_zero(n, k):
    return n & ~(1 << k)

def set_last_bit_to_zero(n):
    return n & (n-1)

def set_all_one_bit_to_zero_except_last(n):
    return n & -n

def store_set_using_bit(nums):
    res = 0
    for num in nums:
        res = res | 1 << num
    return res

def create_set_from_bit(res):
    sets = set()
    for i in range(33):
        if res & (1 << i):
            sets.add(i)
    return sets

r = store_set_using_bit([12,3,4])
sets = create_set_from_bit(r)
assert r == 1 << 12 | 1 << 3 | 1 << 4
assert sets == {12, 3, 4}

def hamming(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
    return count

def hamming_bit(n1, n2):
    """
    note:
    xor 1 if kth digit in n1 and n2 are different
    bitwise operator return value, it does not mutate variable
    """
    res = n1 ^ n2
    dst = 0
    while res:
        dst += res & 1
        res = res >> 1
    return dst

assert hamming_bit(4, 8) == 2

class CountSubGrid:
    """
    calculate the number of subgrids
    whose all corners are black.
    """
    def count_sub_grid(self, board):
        bit_board = self.create_bit_board(board)


    def create_bit_board(self, board):
        """
        divide columns of board into block, each block hold N-bits represent color of block
        """
        N = 3
        bit_boards = []
        for row in range(len(board)):
            count = 0
            bit_row = list()
            for col in range(len(board[0])):
                val = board[row][col]
                count +=  val << (col % N)
                if col % N == 2:
                    bit_row.append(count)
                    count = 0
            bit_boards.append(bit_row)

        return bit_boards

    def pop_count(self, n):
        """
        calculate number of 1 bit in integer n
        """
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

csg = CountSubGrid()
board1 = [[1, 1, 0, 1, 1, 1, 0, 0, 0]]
bit_board1 = csg.create_bit_board(board1)
board2 = [[1, 1, 0, 1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0, 1, 0]]
bit_board2 = csg.create_bit_board(board2)

assert bit_board1 == [[3, 7, 0]]
assert bit_board2 == [[3, 7, 0], [3, 7, 2]]

assert csg.pop_count(1) == 1
assert csg.pop_count(10) == 2