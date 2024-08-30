def convertVariables(file_path, variables_path):
    with open(variables_path, 'r') as file:
        variables = file.readlines()
    for i in range(len(variables)):
        variables[i] = variables[i].replace('\n', '')
    with open(file_path, 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        for j in range(len(variables)):
            var_array = variables[j].split('|')
            if var_array[0] in data[i]:
                # print('var_array[0]: ', var_array[0])
                # print('var_array[1]: ', var_array[1])
                if var_array[1] == 'delete':
                    data[i] = ''
                data[i] = data[i].replace(var_array[0], var_array[1])
    with open(file_path, 'w') as file:
        file.writelines(data)

