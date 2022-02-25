def containsNearbyDuplicate_brute_force(nums, k):
    """
    brute force, use two pointer to shifting window, look out for all possibility
    time complexity: O(N**2)
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            distance = abs(i-j)
            if  distance > k:
                break
            elif nums[i] == nums[j]:
                return True
    return False

def containsNearbyDuplicate(nums, k):
    """
    use set to remember value within k
    time complexity: O(N)
    """
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True

        seen.add(nums[i])

        # if we have seen element more than k shrink it to k
        if len(seen) > k:
            seen.remove(nums[i-k])
    return False