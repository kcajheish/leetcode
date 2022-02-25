from typing import List
class Solution:
    def minMutationBFS(self, start: str, end: str, bank: List[str]) -> int:
        # if genens does not have same length, no way it can mutate
        if len(start) != len(end):
            return -1

        queue = [(start, 0)]
        bank_set = set(bank)
        while queue:
            current, num = queue.pop(0)

            # return number of mutation if mutation achieves end results.
            if current == end:
                return num

            # mutate on gene at a time in sequece
            ## if mutation is in the bank, remove it to mark the mutation as visited
            for i in range(len(current)):
                for gene in 'ACTG':
                    mutation = current[:i] + gene + current[i+1:]
                    if mutation in bank_set:
                        bank_set.remove(mutation)
                        queue.append((mutation, num+1))
        return -1
