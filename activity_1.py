with open('Codingal (2).txt', 'w') as file:
    file.write('Hi i am Bharath.')
file.close()

with open('Codingal (2).txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()