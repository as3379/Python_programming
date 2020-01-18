"""string problem to remove numbers from a mix of numbers and characters
"""
string = 'This string is not yet perfect1234 and 123pretty but it can be.'

CorrectedString = ""
for characters in string:
    if characters.isdigit():
        continue #Skipping charactewr if it is a number
    CorrectedString += characters
print(CorrectedString)
