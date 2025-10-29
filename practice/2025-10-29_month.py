'''
This program print the abbreviation of a month, given it a number
'''

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

def main():
    try:
        n = input("Enter a month number (1-12): ")
        n_int = int(n)

        pos = (n_int-1) * 3

        month_abbrev = months[pos: pos+3]

        print(f"The month abbreviation is {month_abbrev}.")
    
    except ValueError:
        print(f"Invalid Input: Your input [{n}] is not a valid input (1-12).")

main()