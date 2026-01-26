from pathlib import Path, PurePath, PosixPath, PurePosixPath, WindowsPath, PureWindowsPath

"""
pathlib provides object oriented approch to handle file system unlike os library that handles filesystem as strings.
"""

# We can initialize a path using Path("...")
p1= Path('.')
print(p1)

# Primary thing to remember is difference between absolute and relative path
# p1 is a relative path that points to the current working directory "." and it depends on where the script is run

p2 = Path("main/data.txt")
print(p2)
# p2 is also relative path 

print(p1.absolute())

'''
Output:
C:\\Users\HP\Documents\Python\Libraries

This is a absolute path that indicated to the root (and drive on Windows path) and is independent of where the script runs
'''

p3 = Path('C:/root/user/main')
# p3 is an abosolute path as it starts with '/' root

p4 = PurePosixPath("/root/user")
# This is an absolute unix path
# Posix refers to Unix based filesystem representation. It does not have drive "c: d:" as in windows 
"""
PurePath provides pathhandling operations without accessing the file

PosixPath doesn't work on Windows System so i have used PurePosixPath
"""

p5 = WindowsPath("/root/user")
# This is not an absolute path as Windows path reqires the drive part

print(p1.is_absolute())
print(p2.is_absolute())
print(p3.is_absolute())
print(p4.is_absolute())
print(p5.is_absolute())
# We can tell a path is absolute or not using .is_absolute() method

"""
Output:
False
False
True
True
False
"""

# -------------------------------------------------------------------------------------------------------------------------

path = Path()
# An empty Path() always indicated towards the current working directory "."
print(path)

p = Path.cwd()
# We can get the absolute path of current working directory using Path.cwd() method
print(p)

# -------------------------------------------------------------------------------------------------------------------------

p = Path('main/index.txt')

print(p.exists())
# Check if a directory or file exists

print(p.is_file())
print(p.is_dir())
# Check if the path is a file or a directory
# If the path doesnot exist it will show false for both file and directory

# -------------------------------------------------------------------------------------------------------------------------

p = Path('.')
q = p / "main" / "hash"
# q = p.joinpath("main", "hash")

print(p)
print(q)
# We can join path using / sign or using .joinpath("...") method 

# -------------------------------------------------------------------------------------------------------------------------

p = Path("C:/User/Document/Python/main.py")
q = Path("./main/main.py")

print(p.parts)
# all parts in a path
print(p.name) # name of the path here main.py is the path name
print(p.suffix) # suffix from path name
print(p.stem) # path name without the suffix
print(p.parent) # parent of path ;entire parent path to drive/root in absolute path
print(p.parent.parent) # parent of Python 
print(q.parent) # prints to the current working directory in relative path
print(q.parent.parent)
print(p.root) # root of path
print(p.drive) # drive in path
print(p.anchor) # drive + root

# -------------------------------------------------------------------------------------------------------------------------

p = Path("Documents/../Home")
q = Path("~/Desktop/Python")
# ".." represents the parent directory and "~" represents the user's home directory.
# These symbols are not automatically interpreted.

print(p.absolute())
# Output: C:\Users\HP\Desktop\Python\Libraries\Documents\..\Home

print(q.absolute())
# Output: C:\Users\HP\Desktop\Python\Libraries\~\Desktop\Python

# .absolute() converts a path to an absolute path based on the current working directory.
# It does NOT resolve "..", ".", or "~" — they are treated as normal path parts.

print(p.resolve())
# Output: C:\Users\HP\Desktop\Python\Libraries\Home
# .resolve() converts a path to an absolute path and resolves ".." and "." by normalizing the path.
# It also resolves symbolic links.

print(q.resolve())
# Output: C:\Users\HP\Desktop\Python\Libraries\~\Desktop\Python
# .resolve() converts a path to an absolute, normalized path
# and resolves "." and "..".
# It does NOT expand "~".

print(q.expanduser())
# Output: C:\Users\HP\Desktop\Python
# .expanduser() expands "~" to the user's home directory.
# It does not resolve ".." or make the path absolute by itself.

# -------------------------------------------------------------------------------------------------------------------------

p = Path("root")
print(".root exists", p.exists())
p.mkdir()
# mkdir() creates a directory.
# By default, it creates only the last directory and raises an error if the directory already exists or if parent directories are missing.
print(".root exists", p.exists())

p = Path("root/main")
print(".root/main exists", p.exists())
p.mkdir(parents=True, exist_ok=True)
# parents=True allows creation of missing parent directories.
# exist_ok=True prevents an error if the directory already exists.
print(".root/main exists", p.exists())

p.rmdir()
# rmdir() removes/deletes the last directory of path only if the directory is empty
# Returns an error if the directory is not empty

p.parent.rmdir()
# removes the parent of last directory

p = Path("main/init")
p.mkdir(parents=True, exist_ok=True)

print("init.txt exists", q.exists())
q = p / "init.txt"
q.touch()
# touch() creates file 
print("init.txt exists", q.exists())

text_input = f"Initialization start in {', '.join(str(x) for x in range(1, 4))}"
q.write_text(text_input)
# .write_text writes text in file 

text_output = q.read_text()
print(text_output)
# .read_text reads the text info from the file 

byte_input = b"\x89PNG\r\n\x1a\n"
q .write_bytes(byte_input)
# .write_bytes writes byte data 

byte_output = q.read_bytes()
print(byte_output)
# .read_bytes() reads the byte data from file 

# .write_bytes and .write_text method replace the text and byte instead of appending data 
# use file handling to append info

print(q.name)
q = q.rename("main/init/__init__.txt")
# renames the file and raise error if new file name exists before
# also can do q.replace()
print(q.name)

q.write_text("")

with q.open("a") as f:
    for x in range(3, 0, -1):
        f.write(f"Initialization {x}\n")

with q.open() as f:
    content = f.read()

print(content)

print("init.txt exists", q.exists())
q.unlink()
print("init.txt exists", q.exists())
# .unlink() deletes file 

# -------------------------------------------------------------------------------------------------------------------------

p = Path()

for x in p.iterdir():
    # iterdir() iterates over the files and folder in the path and returns their file name 
    # iterdir() does not check child files and folder
    if x.is_file():
        print(f"file: {x}")
    if x.is_dir():
        print(f"folder: {x}")

for x in p.glob("*.py"):
    # glob() searches for file using shell style pattern
    # *.py means ends in .py 
    print(f"Python file {x}")

print("\n")
for x in p.glob("??[a-f]*.py"):
    # ? represents one character, ?? represents two character
    # [a-f] represents specific a character from a to f
    print(f"file {x}")

print('\n')
for x in p.rglob("*"):
    # .rglob() is recursive glob that searches child files as well
    # you can also do glob("**/*") instead of rglob()
    if x.is_file():
        print(f"file: {x}")
    if x.is_dir():
        print(f"folder: {x}")