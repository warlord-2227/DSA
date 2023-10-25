"""
Write a program that comuptes amount of bank amount from a transaction log
"""
#import sys 
#user_input =sys.stdin.read()
print("Enter your logs ")
transactions = [] 
x = input()
while x!='':
    transactions.append(x)
    x = input()

answer = 0 
for i in transactions:
    log = i.split(" ")
    if log[0] == "D":
        answer += int(log[1])
    elif log[0]=="W":
        answer -= int(log[1])

print(answer)
