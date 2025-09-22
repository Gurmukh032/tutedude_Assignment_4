file = "C:/Users/Gurmukhupkar.Singh/Desktop/Python/ASSIGNMENT 1/sample.txt"
try:
    with open(file, "r") as f:
        print("Reading file content:")
        print(f.read())
except:
    print("Error: The file 'sample.txt' was not found.")