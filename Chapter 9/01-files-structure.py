#* FILE I/O in Python
#^ It stands for File Input and Output

#* Input = Reading data from a file
#* Output = Writing data to a file

#* File modes used in open():
#* 'w' - Write (overwrites file or creates new)
#^ Example: open("file.txt", "w")
#* 'r' - Read
#^ Example: open("file.txt", "r")
#* 'a' - Append (adds at the end of file)
#^ Example: open("file.txt", "a")
#* 'x' - Create (gives error if file already exists)
#^ Example: open("file.txt", "x")
#* 'b' - Binary mode (used for images, PDFs)
#^ Example: open("file.txt", "rb")
#* 't' - Text mode (default mode)
#^ Example: open("file.txt", "rt")

#* Example 1: Create & Write to a File
with open("note.txt", "w") as f:  #^ Opens file in write mode
    f.write("Hello! This file is created using Python.")  #^ Writes content

#* Example 2: Read from a File
with open("note.txt", "r") as f:  #^ Opens file in read mode
    content = f.read()  #^ Reads the full content
    print(content)  #^ Prints file content

#* Example 3: Append to a File
with open("note.txt", "a") as f:  #^ Opens file in append mode
    f.write("\nThis line is added later.")  #^ Appends new content

#* Example 4: Read a Line from File
with open("note.txt", "r") as f:  #^ Reopen to read
    line = f.readline()  #^ Reads the first line
    print("First Line:", line)

#* Example 5: tell() - Current file pointer position
with open("note.txt", "r") as f:
    f.read(10)  #^ Read first 10 characters
    pos = f.tell()  #^ Get current pointer position
    print("Pointer at:", pos)

#* Example 6: readlines() - Read all lines into list
with open("note.txt", "r") as f:
    lines = f.readlines()  #^ Each line becomes a list item
    print("All Lines:", lines)
