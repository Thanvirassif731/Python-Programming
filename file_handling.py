import re

fname = input("Enter the file name : ")

num_words = 0


with open(fname, 'r') as file:
    data = file.read()                                                          # Reads the text
    print(data)

    lines = data.split()
    num_words += len(lines)                                                     # Number of words
    print(f"Total number of words : {num_words}")

    tot_numeric = re.findall(r"\d+", data)
    numeric = len(tot_numeric)                                                  # Number of Numerics
    print(f"Total number of Numerics : {numeric}")                              # prints total numerics

    not_special_char = sum(not data.isalnum() for c in data)                    # Number of Letters {I have used special characters method and setted 'NOT'
    print(f"Total number of letters : {not_special_char}")

    special_characters = re.findall("[^a-zA-Z0-9 ]", data)                      # Number of special Characters
    special_char_count = len(special_characters)
    print(f"Total number of Special Characters : {special_char_count}")         # prints total Special char



    print(f"\n\nspecial characters are Filtered : {special_characters}")            # prints the filtered special char
    print(f"Numerics are filtered : {tot_numeric}")                             # prints the filtered numerics

file.close()
