fname = input("Enter the file name : ")

num_words = 0

# Search the file that we gave through input...
with open(fname,'r') as file:
    # Assign the file contents and reads the text in it...
    data = file.read()
    print(data)
    # Lines going to split...
    lines = data.split()
    num_words += len(lines)

# Finally, Printing the total numbers of words in the text file...
print("Number of words:")
print(num_words)
file.close()