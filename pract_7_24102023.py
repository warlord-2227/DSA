"""
Write a program that takes two comma seperated inputs and returns multi dimensional array where rows and columnes relations are i*j 
i = 0,1,2,..,X-1; 
j = 0,1,2,..,Y-1
"""
nums = input("Enter comma seperated two numbers only:").split(",")
rows = int(nums[0])
columns = int(nums[-1])
answer = []
for i in range(rows):
    temp_row = []
    for j in range(columns):
        temp_row.append(i*j)
    answer.append(temp_row)

print(answer)
