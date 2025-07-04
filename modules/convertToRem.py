# import subprocess

# from libs.buffer import addToClipBoardFile
def convertToRem(file_path):
    ## find in file_path px and divide by 10 and write rem
    with open(file_path, "r") as file:
        data = file.readlines()
    for i in range(len(data)):
        if "px" in data[i]:
            ignored_props = [
                "border: 1px",
                "max-width",
                "linear-gradient",
                "&",
                "width: 0.1rem ;",
                "height: 1px;",
            ]
            if any(prop in data[i] for prop in ignored_props):
                continue
            else:
                arr = data[i].split(" ")
                for j in range(len(arr)):
                    if "px" in arr[j]:
                        elem = arr[j]
                        if ";" in arr[j]:
                            arr[j] = arr[j].replace(";", "")
                        number = float(arr[j].replace("px", "")) / 10
                        if ";" in elem:
                            arr[j] = str(number) + "rem;"
                        else:
                            arr[j] = str(number) + "rem"
                data[i] = " ".join(arr) + "\n"
        else:
            data[i] = data[i]
    with open(file_path, "w") as file:
        file.writelines(data)
