from read_file import read_file
from write_file import write_file
from append_write import append_write

read_file("example.txt")
append_write("example.txt", "This is a test.\n")
read_file("example.txt")
write_file("example.txt", "This is a new test.\n")
read_file("example.txt")