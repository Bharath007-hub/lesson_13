new_file = open('n_file.txt','x')
new_file.close()

import os
print("Checking if n_file exists or not....")
if os.path.exists("n_file.txt"):
    os.remove("n_file.txt")
else:
    print("The file does not exist.")

    my_file = open('n_file.txt','w')
    my_file.write("Hi i am bharath.")
    my_file.close()

    os.remove('n_file.txt')
    os.rmdir('Folder')