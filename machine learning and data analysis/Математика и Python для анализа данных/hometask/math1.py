import scipy
from scipy import spatial
import re

with open('sentences.txt', 'r') as file:
     sentences = file.read().rstrip('\n').lower()

# create word and sentences list
sentences_list = sentences.split('\n')
word_list = []
for word in re.split('[^a-z]', sentences):
    if word not in word_list:
        word_list.append(word)
word_list.pop(4)

frame = [[0] * 254 for i in range(22)]

for sentence in sentences_list:
    for word in word_list:
        for index in re.split('[^a-z]', sentence):
            if index == word:
                frame[sentences_list.index(sentence)][word_list.index(word)] += 1

# output
for row in frame:
    for element in row:
        print(element, end=' ')
    print()

# some math
distance = []
min1, min2 = 1, 1
for index in range(1, len(sentences_list)):
    tmp = scipy.spatial.distance.cosine(frame[0], frame[index])
    distance.append(tmp)
    if tmp < min2:
        if tmp < min1:
            if min1 < min2:
                min2 = min1
            min1 = tmp
            continue
        min2 = tmp
print(min1,min2)
print(distance.index(min2), distance.index(min1))
