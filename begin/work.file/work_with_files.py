f = open("myfile", "w")
f.write("First line with necessary newline character\n") # 44
f.write("Second line to write to the file\n") # 33
f.close()

f.open("myfile", "r")
line1 = f.readline()
line2 = f.readline()
f.close()

print(line1, line2)
'''
First line with necessary newline character
Second line to write to the file
'''


import os

print(os.getcwd()) # Desktop/python-project/python-express