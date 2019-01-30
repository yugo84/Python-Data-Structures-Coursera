fname=input('enter file name :')
fh=open(fname)
list1=[]
for i in fh:
    line=i.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index=line.find('0')
    list1.append(float(line[index:]))
length=len(list1)
print("Average spam : ", sum(list1)/length)
