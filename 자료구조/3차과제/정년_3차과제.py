# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:10:33 2021

@author: bhs89
"""

table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
         ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
         ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), 
         ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
         ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
         ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..')]

class MorseTree:
    
    def __init__(self, char="", left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

def encoder(ch):
    ch_mo = table[ord(ch) - ord("A")][1]
    return ch_mo

def decoder(morse_tree, strmo, i=0):
    if i == len(strmo):
        return morse_tree.char
    elif strmo[i] == '.':
        return decoder(morse_tree.left, strmo, i+1)
    else:
        return decoder(morse_tree.right, strmo, i+1) 

morse_tree = MorseTree('',
                MorseTree('E',
                     MorseTree('I',
                          MorseTree('S',
                               MorseTree('H'),
                               MorseTree('V')),
                          MorseTree('U',
                               MorseTree('F'))),
                     MorseTree('A',
                          MorseTree('R',
                               MorseTree('L')),
                          MorseTree('W',
                               MorseTree('P'),
                               MorseTree('J')))),
                MorseTree('T',
                     MorseTree('N',
                          MorseTree('D',
                               MorseTree('B'),
                               MorseTree('X')),
                          MorseTree('K',
                               MorseTree('C'),
                               MorseTree('Y'))),
                     MorseTree('M',
                          MorseTree('G',
                               MorseTree('Z'),
                               MorseTree('Q')),
                          MorseTree('O'))))

strin = input("입력 문장 : ")

listin = list(strin)
listmo = []
listout = []

for ch in listin:
    listmo.append(encoder(ch))
print("Morse Code :", listmo)

for morse in listmo:
    listout.append(decoder(morse_tree, morse))
print("Decoding : " + "".join(listout))