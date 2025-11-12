def happy():
    print("Happy birthday to you!")
def singFred():
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()

singFred()

def singLucy():
    happy()
    happy()
    print("Happy birthday, dear Lucy...")
    happy()

def main():
    singFred()
    print()
    singLucy()
    
def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()

def main():
    sing("Fred")
    print()
    sing("Lucy")


