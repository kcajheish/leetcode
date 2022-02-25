def checkInclusion(s1, s2):
    """
    sliding window
    s1, s2 has length of M, N respectively.
    time complexity: MN
    space complexity: M
    """
    def is_meet(counter):
        for char in counter:
            if counter[char] > 0:
                return False
        return True

    counter = {}
    for char in s1:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1

    l, r = 0, 0
    while r < len(s2):
        char_r = s2[r]
        char_l = s2[l]
        if char_r in counter:
            counter[char_r] -= 1
            if is_meet(counter):
                return True
        # sliding window
        if r - l + 1 < len(s1):
            r += 1
        else:
            if char_l in counter:
                counter[char_l] += 1
            l += 1
            r += 1
    return False
s1 = "ab"
s2 = "eidboaoo"
r = checkInclusion(s1, s2)
print(r)