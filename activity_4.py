with open('Codingal (2).txt')as fp:
    data1 = fp.read()
with open('my_file.txt')as fp:
    data2 = fp.read()

data1 += '\n'
data1+= data2
print("Merging two files..")
with open("Merged_file.txt", 'w') as fp:
    fp.write(data1)
    