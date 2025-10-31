'''
a) for ch in "aardvark": 
print (ch) 
b) for w in "Now is the winter of our discontent . . ". split() : 
print (w) 
c) for w in "Mississippi". split (" i") : 
print (w, end=" ") 
d) msg = "" 
for s in "secret".split("e") : 
msg = msg + s 
print(msg) 
e) msg = "" 
for ch in "secret": 
msg = msg + chr(ord(ch)+1) 
print(msg)

'''

print("a)\n")
for ch in "aardvark": 
    print (ch)
print("========\n")


print("b)\n")
for w in "Now is the winter of our discontent . . ".split(): 
    print (w)
print("========\n")

print("c)\n")
for w in "Mississippi". split ("i"): 
    print (w, end=" ")
print()
print("========\n")

print("d)\n")
msg = "" 
for s in "secret".split("e") : 
    msg = msg + s 
print(msg)
print("========\n")


print("e)\n")
msg = "" 
for ch in "secret": 
    msg = msg + chr(ord(ch)+1) 
print(msg)
print("========\n")