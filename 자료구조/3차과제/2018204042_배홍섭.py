# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:38:58 2021

@author: bhs89
"""

table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
         ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
         ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), 
         ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
         ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
         ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..')]

#이진트리 클래스 생성
class morsebinarytree:
    
    def __init__(self, element,left=None, right=None):
        self.element = element
        self.left = left
        self.right = right
        
def encoder (i):
    morse = table[ord(i) - 65][1] #아스키코드 활용
    return morse

#재귀함수를 통한 binaryTree탐색
def decoder (tree,morse,i=0):
    if i == len(morse): 
        return tree.element
    if morse[i] == '.':
        return decoder(tree.left,morse,i+1)
    elif morse[i] == '-':
        return decoder(tree.right,morse,i+1)

#main
sentence = input("입력 문장 : ")
morse_code = []

for i in sentence:
    morse_code.append(encoder(i))
print("Morse Code : ", morse_code)

#이진트리 구조 구현
morse_tree = morsebinarytree('',
                morsebinarytree('E',
                     morsebinarytree('I',
                          morsebinarytree('S',
                               morsebinarytree('H'),
                               morsebinarytree('V')),
                          morsebinarytree('U',
                               morsebinarytree('F'))),
                     morsebinarytree('A',
                          morsebinarytree('R',
                               morsebinarytree('L')),
                          morsebinarytree('W',
                               morsebinarytree('P'),
                               morsebinarytree('J')))),
                morsebinarytree('T',
                     morsebinarytree('N',
                          morsebinarytree('D',
                               morsebinarytree('B'),
                               morsebinarytree('X')),
                          morsebinarytree('K',
                               morsebinarytree('C'),
                               morsebinarytree('Y'))),
                     morsebinarytree('M',
                          morsebinarytree('G',
                               morsebinarytree('Z'),
                               morsebinarytree('Q')),
                          morsebinarytree('O'))))

morse_list = ''
for j in morse_code:
    morse_list += decoder(morse_tree,j)
print("Decoding : ",morse_list)