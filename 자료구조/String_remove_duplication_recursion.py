# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def remove_duplicate_letters(s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char) :]
        # 전체 집합과 접미사 집합이 일치할때 분리 진행
        if set(s) == set(suffix):
            return char + remove_duplicate_letters(suffix.replace(char, ""))
    return ""


string = input("Input = ")
print("Result: ", remove_duplicate_letters(string))