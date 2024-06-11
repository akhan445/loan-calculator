from math import ceil, log
import argparse


def nominal_interest_rate(interest_rate):
    return interest_rate / (12 * 100)


def calculate_principal(annuity_payment, periods, interest):
    i = nominal_interest_rate(interest)
    loan_principal = annuity_payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))

    return int(loan_principal)


def calculate_annuity_payment(principal, periods, interest):
    i = nominal_interest_rate(interest)
    annuity_payment = principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))

    return ceil(annuity_payment)


def calculate_num_periods(principal, payment, interest):
    i = nominal_interest_rate(interest)

    num_months = log((payment / (payment - i * principal)), 1 + i)

    return ceil(num_months)


def generate_message(years, months):
    message = "It will take"

    if years == 1:
        message += " 1 year"
    elif years > 1:
        message += f' {years} years'

    if months == 1:
        message += ' 1 month'
    elif months > 1:
        message += f' {months} months'

    message += ' to repay this loan!'
    return message


parser = argparse.ArgumentParser(
    prog='LoanCalculator',
    description='Personal Finance Loan Calculator',
)

parser.add_argument('--principal', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float, required=True)

args = parser.parse_args()
result = None

if args.principal is None:
    result = calculate_principal(args.payment, args.periods, args.interest)
    print(f'Your loan principal = {result}!')
elif args.payment is None:
    result = calculate_annuity_payment(args.principal, args.periods, args.interest)
    print(f'Your monthly payment = {result}!')
elif args.periods is None:
    result = calculate_num_periods(args.principal, args.payment, args.interest)
    years, months = divmod(result, 12)
    message = generate_message(years, months)
    print(message)