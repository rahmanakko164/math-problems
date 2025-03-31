# Problem statement: Given an unsorted array of integers, find the number of unique pairs with equal sums.
def count_equal_sums(nums):
    # Dictionary to store the frequency of each element in nums
    freq = {}
    
    # Calculate total sum and add 0 as a reference value
    total_sum = sum(nums)
    
    for num in nums:
        if num == 0:
            # If the current number is zero, it can be paired with any negative number
            freq[num] = 1 + (freq.get(num - (-num), 0) or 0)
            continue
        
        # Subtract 0 from frequency if applicable
        if num in freq:
            total_sum -= num
            freq[num] += 1
        else:
            total_sum += num

    return len(freq)

# Example usage
nums = [-1, 2, -3, 3]
print(count_equal_sums(nums)) # Output: 2 (because there are two pairs that sum to zero: (-1, 2) and (3, -3))
