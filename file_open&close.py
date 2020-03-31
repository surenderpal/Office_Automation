f=open('abc.txt',r)
print('file name:',f.name)
print('file mode:',f.mode)
print('Is file closed:',f.closed)
print('Is file Readable:',f.readable)
print('Is file Writeable:'f.writable)
f.close()
print('Is file closed:',f.closed)

