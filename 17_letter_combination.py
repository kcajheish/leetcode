def letterCombinations_dfs(digits):
    """
    time complexity:
    space complexity:
    """
    def backtrack(l, queue, results, mapping):
        if l == len(queue):
            subset = ''.join(queue)
            results.append(subset)
            return

        for char in mapping[digits[l]]:
            queue[l] = char
            backtrack(l+1, queue, results, mapping)

    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    queue = ['' for _ in range(len(digits))]
    results = []

    backtrack(0, queue, results, mapping)
    return results


def letterCombinations_bfs(digits):
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    queue = [""]
    for i, digit in enumerate(digits):
        while len(queue[0]) < i + 1:
            words = queue.pop(0)
            for char in mapping[digit]:
                new_words = words + char
                queue.append(new_words)

    return queue
#r = letterCombinations("23")
