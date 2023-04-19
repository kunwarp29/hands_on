#to get file object use built-in open() command.
f = open('test.txt', 'r')  #open coommand allows us to read, write, append on the file.(if we want read&write then 'r+', for append use 'a')
print(f.name) #o/p: test.txt
print(f.mode)
f.close() #if we are opening the file without context manager then we need to explicitly close the file.
# for line in f:
#     print(line)


'''Using context manager using 'with' keyword and we don't need to explicitly close the file.'''   

with open('test.txt', 'r') as f:    # it is same as f = open('test.txt', 'r')
    pass
  
print(f.closed) #retrns true.
print(f.read()) #ValueError: I/O operation on closed file.