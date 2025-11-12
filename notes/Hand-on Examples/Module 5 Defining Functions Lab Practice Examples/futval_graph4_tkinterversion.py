import matplotlib.pyplot as plt

def main():
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    # Prepare data
    years = list(range(11))
    values = [principal]

    for year in range(1, 11):
        principal = principal * (1 + apr)
        values.append(principal)

    # Plot
    plt.bar(years, values, color="green", width=0.5)
    plt.xlabel("Year")
    plt.ylabel("Investment Value ($)")
    plt.title("Investment Growth Over 10 Years")
    plt.show()

main()
