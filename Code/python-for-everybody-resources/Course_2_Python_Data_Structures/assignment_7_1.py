#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
# Use words.txt as the file name

# Ask the user to input a file name
fname = input("Enter file name: ")
# Open the file with the provided name
fh = open(fname)
# Print the file object (for debugging)
print("fh___", fh)
# Read the whole content of the file
book = fh.read()
# Print the content as-is (in lower case or whatever the original was)
print("book___", book)
# Convert the entire content to uppercase
bookCAPITAL = book.upper()
# Remove any trailing whitespaces (including newlines at the end)
bookCAPITALrstrip = bookCAPITAL.rstrip()
# Print the final result
print(bookCAPITALrstrip)

#==========================
try:
    fname = input("Enter file name: ")
    with open(fname) as fh:
        book = fh.read()
        print(book.upper().rstrip())
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
#==========================
# The above code is a simple file reading and string manipulation program.