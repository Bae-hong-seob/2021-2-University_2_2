# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:34:31 2021

@author: bhs89
"""
import numpy
import sys
from collections import Counter


i = 0
num = [0] * 10
sum = 0
mid = 0
mode = 0
devi = 0
result = 1

while(i < 10):
    print("실수 ",i+1,"개를 입력하세요. (",i+1,"/10) :")

    num[i] = float(input())
    sum+= num[i]
    result = result * num[i]
    i+=1
    
print("전체 개수 : ",len(num))
print("합 : ", sum)
print("평균 : ", sum/10)

sorted(num)
print("중앙값 : ",(num[4]+num[5])/2)

#print("최빈값 : ", numpy.mode(num))
mode = Counter(num)
mode = mode.most_common(1)
print("편차 : ", mode)
    
print("모두를 곱한값 : ",result)


"""def mode(nums: List[float]) -> float:
    count = 0
    mode = 0
    for x in nums:
        if nums.count(x) > count:
            count = nums.count(x)
            mode = x

    return mode


def print_statistics(nums: List[float]):
    nums.sort()
    total_nums = len(nums)
    sum_nums = sum(nums)
    mean_nums = sum(nums) / len(nums)
    median_nums = nums[len(nums) // 2] + nums[-(len(nums) // 2 - 1)]
    mode_nums = mode(nums)
    deviation_nums = sum([(num - (sum(nums) / len(nums))) ** 2 for num in nums])
    multiple_nums = eval("*".join([str(num) for num in nums]))
    print(
        "전체 개수 {}개, 합 {}, 평균 {}, 중앙값 {}, 최빈값 {}, 편차 {} 모두 곱한 값 {}".format(
            total_nums,
            sum_nums,
            mean_nums,
            median_nums,
            mode_nums,
            deviation_nums,
            multiple_nums,
        )
    )


num_list = [int(input(f"실수 10개를 입력하세요. ({i}/10): ")) for i in range(1, 10 + 1)]

print_statistics(num_list) 
"""