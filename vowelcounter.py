# for loops
name="shreyas"
for letters in name:
    print(letters)

for i in range(1,11):
    print(i)
# using nested for loops to create multeplication table
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print("")   

#using break in for loops 
cities=["bengaluru","davangere","hubbli","channagere"]
for index,city in enumerate(cities):
    print(f"cite-{index+1} is {city}")

total=0
i=1
for tatal in range(0,10):
    total=total+tatal
print(total)

a=input("Enter your name :").lower()
vowels=["a","e","i","o","u"]
vowel_count=0
for letter in a:
    if letter in vowels:
        vowel_count+=1

print(f"no of vowels = {vowel_count}")

import time
for i in range(10):
    print(i)
    time.sleep(1)
 