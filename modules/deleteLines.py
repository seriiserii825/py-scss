def deleteLines(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        to_delete = ['font-style: normal', 'line-height: normal', 'font-feature-settings', 'text-overflow', 'overflow']
        if any(prop in data[i] for prop in to_delete):
            data[i] = ''
    with open(file_path, 'w') as file:
        file.writelines(data)
