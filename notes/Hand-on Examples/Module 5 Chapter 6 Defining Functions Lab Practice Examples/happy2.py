# happy2.py
#In addition to being more elegant, this version of the program is also more flexible than the original because the printing is no longer distributed across multiple functions. For example, we can easily modify the program to write the results into a file instead of to the screen.
#All we have to do is open a file for writing and add a file= parameter to the print statement.

def happy(): 
    return "Happy Birthday to you!\n"

def verseFor(person): 
    lyrics = happy()*2 + "Happy birthday, dear " + person + ". \n" + happy() 
    return lyrics 

def main(): 
    outf = open("Happy_Birthday.txt", "w") 
    for person in ["Fred", "Lucy", "Elmer"]: 
        print(verseFor(person), file=outf) 
    outf.close()

main()
    
"""
def main(): 
    for person in ["Fred", "Lucy", "Elmer"]: 
        print(verseFor(person))
        
main() 
"""
