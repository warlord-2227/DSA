"""
Write a program that takes sequence of comma seperated numbers from console and generate a list and a tuple which contains every number.
"""

ips = input("Enter seqence of number:")
lst_nums = ips.split(",")
tpl_nums = tuple(lst_nums)
print(lst_nums)
print(tpl_nums)


