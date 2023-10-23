"""
Write a program,which will find numbers between 3000 and 4000 such that each digit is even number in that and obtained should be printed in a comma seperated sequence 
"""
answer = []
for i in range(1000,3001,1):
    if (i//1000)%2==0:
        temp_i = i%1000
        if (temp_i//100)%2==0:
            temp_i = i%100
            if (temp_i//10)%2==0:
                temp_i = i%10
                if temp_i%2==0:
                    answer.append(i)

print(answer)


