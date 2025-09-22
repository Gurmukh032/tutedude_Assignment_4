text = input("Enter txt to write to the file: ")
with open("output.txt", "a") as f:
    f.write(text + "\n")
print("Data successfully written to output.txt.")

text1 = input("Enter additional text to append: ")
with open("output.txt", "a") as g:
    g.write(text1 + "\n")
print("Data successfully appended.")

with open("output.txt", "r") as t:
    print("Final content of output.txt:")
    print(t.read())