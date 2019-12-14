fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
mail = dict()
count = 0
key = " "
for line in fh:
    if line.startswith('From '):
        words = line.split()
        for word in words:
            mail[word]= mail.get(word,0)+ 1
            if (mail.get(word) > count):
                key = word

print(word, mail.get(word))
