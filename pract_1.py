"""
Write a program which finds all the numbers which are divisible by 7 but not multiple of 5 between 2000 and 3200(both included)
Numbers obtained should be comma seperated sequence on a single line
"""

answer = []
for i in range(2000,3201):
    if (i%7==0) &(i%5!=0):
        answer.append(str(i))
#print(answer)
# Answer in comma seperated sequence 
final_answer =",".join(answer)
print(final_answer)
