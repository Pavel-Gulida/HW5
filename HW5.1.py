import keyword
import string

name = input("Enter name: ")
right = True

if name in keyword.kwlist:
    right = False
if "9" >= name[0] >= "0":
    right = False
if name.count("_") > 1:
    right = False

for letter in name:
    if "Z" >= letter >= "A":
        right = False
        break
    if letter in string.punctuation + " " and letter != "_":
        right = False
        break

print(right)
