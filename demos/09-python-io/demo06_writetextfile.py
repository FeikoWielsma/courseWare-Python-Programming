# writing a text file
fw = open("textfilepolish.txt", mode="w", encoding="UTF-8")
s = "Polish text: ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
fw.write(s)
fw.close()

# reading a text file
fr = open("textfilepolish.txt", mode="r", encoding="UTF-8")
data = fr.read()
# print(repr(data))
print(data)
fr.close()
