#to print the most common word in a file using dictionary 
fname=input('enter the file name :')
fhandle=open(fname)
dict1={}
for line in fhandle:
    words=line.split()
    for word in words:
        dict1[word]=dict1.get(word,0)+1
print(dict1)

lvalue=-99
lkey=None
for k,v in dict1.items():
    if v>lvalue:
        lvalue=v
        lkey=k
print(lkey, lvalue)
