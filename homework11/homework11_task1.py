# create a script in which we specify to write a certain string in a text file
# Since there is no file with this name, it will be created
with open('myfile.txt', 'w') as file_object:
    file_object.write('Hello file world!')

# write a script that tells you to open the file and display what is written in it
with open('myfile.txt', 'r') as file_object:
    print(file_object.read())

# a new text file was created in the same directory where the scripts were run