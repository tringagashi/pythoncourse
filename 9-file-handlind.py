# Writing to file
with open("example.txt", "w") as file:
    file.write("Hello from Python file handling!")

# Reading from file
with open("example.txt", "r") as file:
    content = file.read()

print("File content:", content)
