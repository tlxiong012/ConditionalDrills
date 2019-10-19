'''For this assignment you should look at the variables create below and find the error.
For each task, there will be one error that you must find and correct.
Sometimes there will be an explanation of the problem and/or tips 
that can help you complete the tasks.'''
from Tools.scripts.findnocoding import has_correct_encoding

#1)
#Broken: line 11 is incorrect
#x = 2
#y = 8
#if x < y
#    st = "x is less than y"
#print(st)
#Correct:
if x<y:
    print("x is less than y")

#2)
#Broken: using st instead of print
#x = 2
#y = 8
#if x < y
#    st = "x is less than y"
#else:
#st = "x is greater than y"
#print(st)
#Correct:
if x<y 
    print("x is less than y")
else:
    print("x is greater than y")

#3)
#Broken:
missing parenthesis, indents and other if statements    
#if age < 0:
#   print "This can hardly be true!"
#   elif age == 1:
#   print "about 14 human years"
#   elif age == 2:
#   print "about 22 human years"
#   elif age > 2:
#   human = 22 + (age -2)*5
#   print "Human years: ", human
Correct
if age<0:
    print("this can hardly be true!")
elif age ==1
    print("about 14 human years")
... and so on