outputFile = open('Codingal (2).txt', 'w')
inputFile = open("my_file.txt", 'r')

lines_seen_so_far = set()
print('Eliminating duplicate lines...')
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
inputFile.close()
outputFile.close()