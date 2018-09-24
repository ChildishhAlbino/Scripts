import pyperclip

string = pyperclip.paste()
string2 = ""
i = 0
for i in range (0, len(string)):
    string2 += string[i] + " "
    i += 1
    
pyperclip.copy(string2)
print(string2)

