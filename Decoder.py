import time
import os
string = input("Enter the code >> ")
values = string.split(" ")
decoad = "" 
for extract in values:
    decoad += f"{chr(int(extract))}"
print('Decoding....')
time.sleep(3)
os.system('color b')
print(decoad)
input('')