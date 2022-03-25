
# Given a map of superhero and their power, return the superpower duo who'll be strongest together i.e. max of length(power[i]) * length(power[j]) where the two powers do not share common letters. If no such two superhero exist, return 0.

# e.g. 1:
# { superman: "abcw", batman: "baz", aquaman: "foo", flash: "bar", wonderwoman: "xtfn",martian: "abcdef" }

# Output: 16 superman wonderwoman
# Explanation: The two words can be "abcw", "xtfn", so len("abcw") * len("xtfn") = 16

# n no. of superhero
# m is the max length of power
def greatest_power(power):
    """
    time complexity: O(nm + n^2)
    space complexity: O(n)
    """
    result = []
    for hero in power:
        count = [0] * 26
        for p in power[hero]:
            count[ord(p)-ord('a')] += 1
        result.append(count)

    largest = -1
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            a, b = 0, 0
            for k in range(26):
                if result[i][k] and result[j][k]:
                    break
                elif result[i][k]:
                    a += 1
                elif result[j][k]:
                    b += 1
            if a or b:
                largest = max(largest, a*b)
    return 0 if largest == -1 else largest

def greatest_powerv2(power):
    """
    time complexity: O(nm)
    space complexity: O(nm + n^2m)
    """
    hero = list(power.keys())
    ability = [set(power[h]) for h in hero]
    largest = -1
    for i in range(len(hero)):
        for j in range(1, len(hero)):
            is_overlap = False
            for a in ability[i]:
                is_overlap =  a in ability[j]
                if is_overlap:
                    break
            if not is_overlap:
                largest = max(largest, len(power[hero[i]])*len(power[hero[i]]))
    return 0 if largest == -1 else largest

actual = greatest_powerv2({ 'superman': "abcw", 'batman': "baz", 'aquaman': "foo", 'flash': "bar", 'wonderwoman': "xtfn",'martian': "abcdef" })
assert actual == 16
actual = greatest_powerv2({ 'superman': "abcw", 'batman': "baz", 'aquaman': "foo", 'flash': "bar", 'wonderwoman': "xtfn",'martian': "abcdef" })
assert actual == 16
