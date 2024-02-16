f = open('/Users/i/Desktop/file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)

with open('/Users/i/Desktop/file.txt', 'r') as f:
    print(f.read())
