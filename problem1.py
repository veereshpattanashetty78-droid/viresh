def second_largest(nums):
    if len(nums) < 2:
        return None
    first = second = float()
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float() else None
second_largest([3, 1, 6, 4, 5, 9, 7])
ref=second_largest
print("Second largest num :",ref)
