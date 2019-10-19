try:
    with open("myfile.txt") as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError as ex:
    print("The Data File is missing")
except PermissionError as px:
    print("This is not allowed")
