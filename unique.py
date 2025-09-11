names={}
while True:
    name = input("Name: ")
    if (name==""):
        break
    elif name in names:
        names[name]=names[name]+1
        #raise KeyError("Already got that one!")
    else:
        names[name]=1

print(names)