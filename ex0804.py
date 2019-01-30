fname=input("enter a file name:")
fhandle=open(fname)
list1=[]
for line in fhandle:
    line.strip()
    words=line.split()
    for word in words:
        if word not in list1:
            list1.append(word)
list1.sort()
print(list1)
