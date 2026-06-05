import random
import string

passwords={}

#load existing
try:
    with open("password.txt", "r") as file:
        for line in file:
              website, pwd = line.strip().split(",")
              passwords[website] = pwd

except FileNotFoundError:
    print("File not found")