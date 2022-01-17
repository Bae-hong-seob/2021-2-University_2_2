# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:24:00 2021

@author: bhs89
"""

from collections import Counter


def remove_duplicate_letters_stack(s: str) -> str:
    counter, stack = Counter(s), []
    seen = set()

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return "".join(stack)

string = input("Input = ")
print("Result: ", remove_duplicate_letters_stack(string))
