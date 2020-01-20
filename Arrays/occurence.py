''' write a program where there are multiple users logging
into the system or file and I want to know the login
Occurrences of the each user . Note :
The file is separated by the commas.
ex: User1 , User2, user1 , user3.........  '''

# Open the file in read mode
text = open("file.csv", "r")

# Create an empty dictionary
d = {}

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character and Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower().strip()

    # Split the line into words
    words = line.split(", ")

# Iterate over each word in line
for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] += 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for k in d:
    print(k, ":", d[k])
