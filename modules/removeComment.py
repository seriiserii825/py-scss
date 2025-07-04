def removeComment(file_path):
    # remove comment in line like /* 28.8px */
    with open(file_path, "r") as file:
        data = file.readlines()
    for i in range(len(data)):
        if "/*" in data[i]:
            data[i] = data[i].split("/*")[0] + "\n"
        else:
            data[i] = data[i]
    with open(file_path, "w") as file:
        file.writelines(data)
