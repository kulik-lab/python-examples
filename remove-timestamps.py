import re


with open('text - add colliders and triggers') as f:
    data = f.read()

text= data.split()
newtext = []

for w in text:
    if re.search(r'\d\d:\d\d:\d\d', w):
        #print("Found")
        continue
    else: newtext.append(w)
print(*newtext)