def reverseWordSentence(Sentence):
    # Splitting the Sentence into list of words.

    words = Sentence.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    n = len(words)

    for i in range (0, n):
        if i%2 !=0:
            words[i]  = words[i][::-1]

        # Joining the new list of words
        # to for a new Sentence
    newSentence = " ".join(words)

    return newSentence

# Driver's Code
Sentence = "GeeksforGeeks is good to learn with you"
# Calling the reverseWordSentence
# Function to get the newSentence
print(reverseWordSentence(Sentence))