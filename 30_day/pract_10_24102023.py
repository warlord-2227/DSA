"""
Write a program that takes sequence of whitespace seperated words as input and prints the words after removing all duplicate words and sorting them alphanumerically
"""
import re

inps = input("Enter words for input:")
inps = inps.strip()
words = re.split("\s+",inps)
cnt = {word:0 for word in words}
print(list(cnt.keys()))
answer = list(cnt.keys())
answer.sort()
out = " ".join(answer)
print(out)



