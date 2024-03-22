def solution(nums):
    answer = 0
    s_nums = set(nums)
    l = len(nums)
    
    if len(s_nums) > l//2:
        answer = l//2
    else:
        answer = len(s_nums)
        
    return answer