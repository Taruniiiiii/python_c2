import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)
import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

import re

txt = "The rain in2839010 Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#####file handling###
#syntax=> file=open(filename,mode)
#ex=open(ex.txt,r)(read)

## if file exists file overwrites 
file=open("m1.txt","w")
file.write("hi im t")
file.close

##with
with open("hi.txt","w") as t:
    t.write("this has varibale name ")
#read
file=open("hi.txt","r")
print(file.read())
file.close()

#adding text or updating text
with open("hi.txt","a")as t:
    t.write("hi yall")
    
##creating a file with x
file=open("tar.txt","x")
file.write("new file created using x")
file.close()