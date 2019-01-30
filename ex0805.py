#to get the count of words used in a file using list
fname=input("enter a file name:")
fhandle=open(fname)
word=[]
count=0
for line in fhandle:

    if line.startswith('From ') and len(line)>1:
        word=line.split()
        print(word[1])
        count+=1
print(count)
