# 1. Import necessary libraries
import argparse

# 2. Define constants for IDR plan parameters
INTEREST_RATE = 0.05  # Annual interest rate (5% for REPAYE)
POVERTY_GUIDELINE = 12690  # Poverty guideline for a single person in 2021
REPAYMENT_PERCENTAGE = 0.10  # Percentage of discretionary income to be paid


# 3. Define a function to calculate the monthly payment
def calculate_monthly_payment(income, family_size):
    # Calculate the discretionary income
    discretionary_income = max(0, income - (family_size - 1) * POVERTY_GUIDELINE)

    # Calculate the monthly payment
    monthly_payment = discretionary_income * REPAYMENT_PERCENTAGE / 12.0

    return monthly_payment


# 4. Define a function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate monthly payments for an IDR plan.")
    parser.add_argument('--income', type=float, required=True, help="Annual income")
    parser.add_argument('--family-size', type=int, required=True, help="Family size")
    return parser.parse_args()


# 5. Define the main function
def main():
    args = parse_arguments()
    income = args.income
    family_size = args.family_size

    # Calculate the monthly payment
    monthly_payment = calculate_monthly_payment(income, family_size)

    # Print the result
    print(f"Estimated monthly payment: ${monthly_payment:.2f}")


if __name__ == "__main__":
    main()
