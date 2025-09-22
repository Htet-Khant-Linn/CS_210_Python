print("Hello, world!")
print("Htet Khant Linn")
print("2+3")
print(2+3)
print(f"2+3 {2+3}")



def hello():
    print("Hello Charles.")
    print("CS_210 is easy.")

hello()


def greet(name):
    print(f"Helllo {name}.")

greet("Charles")
greet("Aung")


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()




