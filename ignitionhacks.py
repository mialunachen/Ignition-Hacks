# -*- coding: utf-8 -*-
"""IgnitionHacks

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pDSJzaFbKeE0Aku-ilTuaXVGjURsxtWj
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from google.colab import files
pictureList = []
uploaded = files.upload()
pictureList.append(uploaded)

plt.figure()
plt.imshow(uploaded) 
plt.show()  # display it

import random

#picks a random word from the words list
words = ['pencil', 'phone', 'waterbottle', 'speaker', 'blanket', 'kpop', 'computer', 'science']

number = random.randint(0,len(words)-1)

word = words[number]
hidden_word = '*'*len(word)
win = False
numOfwrong = 0
picture = 0

#runs the game
used = []
num_of_guesses = 0
while(num_of_guesses < 11):
  print(hidden_word)
  print("Used:",used)
  letter = input("Guess a letter:")
  if letter in used:
    num_of_guesses-=1
    print("You already used this letter before!")
    continue
  elif letter in word:
    for i in range(len(word)):
      if word[i] == letter:
        hidden_word = hidden_word[:i] + letter + hidden_word[i+1:]
    used.append(letter)
    num_of_guesses +=1
  else:
    used.append(letter)
    num_of_guesses +=1
    numOfwrong += 1
    picture = pictureList[numOfwrong]
    
  if hidden_word == word:
    win = True
    break

if win == True:
  print(hidden_word)
  print(used)
  print("You guessed it!")
else:
  print("You lose! The word was " + word)