#title                             :PBD23v2.py
#description                       :PBD-23 Python - Write 100 random characters to txt file.
#author                            :MC
#date                              :02/04/2016
#version                           :0.2
#usage                             :python pyscript.py
#notes                             :
#python_version             	   :3.4.2
 
 
# Import the modules needed to run the script.
import random, string
 
# Open the file to which we are writing the characters to (jm.txt) and assign the contents to the 'target' object.
target = open("C:\PYTHON\PBD 23\jm.txt", 'w')
 
# Write 100 random string characters on new lines in uppercase to the ‘target’ object.
for number in range(0,100):
    target.write(random.choice(string.ascii_uppercase) + "\n")
 
# Close the opened file.
target.close()