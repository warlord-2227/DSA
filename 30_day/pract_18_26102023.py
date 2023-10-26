"""
Website requires user to input passwords and username to register. We have to check if password satisfy some of the conditions or not 
atleast 1 upper,atleast 1 lower case, at least 1 number
at least 1 chracter from [$#@], minimum length of it should be 6 and maximum should be 12
"""
import re
inp = input("Enter possible passwords on comma seperated:" ).split(",")
pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$")
#pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$"
#pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
out = []
for cand in inp:
#    if len(cand)>=6 and len(cand)<=12:
   # mat = re.search(pattern,cand)
   if pattern.fullmatch(cand):
       out.append(cand)
print(out)

        
