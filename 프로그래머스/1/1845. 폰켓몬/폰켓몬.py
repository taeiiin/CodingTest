def solution(nums):
    result = 0
    length = len(set(nums))
    pocket = len(nums)//2
    if pocket < length:
        result = pocket
    else:
        result = length
    return result