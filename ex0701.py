fname=input('enter file name :')
fh=open(fname)
for line in fh:
    newline=line.rstrip()
    print(newline.upper())
