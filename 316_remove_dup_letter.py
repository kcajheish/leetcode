class Solution:
    def removeDuplicateLettersStack(self, s: str) -> str:
        stack = []
        last_seen = { char: i for i, char in enumerate(s)}
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue

            while len(stack) and stack[-1] > char and last_seen[stack[-1]] > i:
                remove_char = stack.pop()
                seen.discard(remove_char)

            stack.append(char)
            seen.add(char)
        return ''.join(stack)