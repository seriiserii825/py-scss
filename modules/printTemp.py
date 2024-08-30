def printTemp(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        print(data[i])

