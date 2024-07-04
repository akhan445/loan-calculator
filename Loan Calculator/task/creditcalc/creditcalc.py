from math import ceil, log
import argparse


def check_program_type(value):
    if value not in ["annuity", "diff"]:
        # raise argparse.ArgumentTypeError("Incorrect Parameters")
        print('Incorrect Parameters')
    return value


def check_positive(value):
    fl_value = float(value)
    if fl_value <= 0.0:
        # raise argparse.ArgumentTypeError("Incorrect Parameters")
        print('Incorrect Parameters')
    return fl_value


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


def generate_annuity_message(years, months):
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


def generate_diff_message(payments, overpayment):
    message = ''

    for i in range(len(payments)):
        message += f'Month {i + 1}: payments is {payments[i]}\n'

    message += f'\nOverpayment = {overpayment}'

    return message


def calculate_differentiated(principal, periods, interest):
    i = nominal_interest_rate(interest)
    payments = []

    for m in range(1, int(periods) + 1):
        D = principal / periods + i * (principal - (principal * (m - 1)) / periods)
        payments.append(ceil(D))

    return payments


parser = argparse.ArgumentParser(
    prog='LoanCalculator',
    description='Personal Finance Loan Calculator',
)

parser.add_argument('--type', type=check_program_type)
parser.add_argument('--principal', type=check_positive)
parser.add_argument('--payment', type=check_positive)
parser.add_argument('--periods', type=check_positive)
parser.add_argument('--interest', type=check_positive)

args = parser.parse_args()

if args.type is None or args.interest is None:
    print('Incorrect Parameters')
elif args.type == "diff":
    # raise error if all the right arguments are not provided
    if not all([args.principal, args.periods, args.interest]):
        # raise argparse.ArgumentTypeError("Incorrect Parameters")
        print('Incorrect Parameters')
    else:
        payments = calculate_differentiated(args.principal, args.periods, args.interest)
        overpayment = sum(payments) - int(args.principal)

        message = generate_diff_message(payments, overpayment)
        print(message)

else:  # annuity
    overpayment = 0

    if args.principal is None:
        loan_principal = calculate_principal(args.payment, args.periods, args.interest)
        print(f'Your loan principal = {loan_principal}!')
        overpayment = ceil(args.payment * args.periods - loan_principal)
    elif args.payment is None:
        ann_payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
        print(f'Your monthly payment = {ann_payment}!')
        overpayment = ceil(ann_payment * args.periods - args.principal)
    elif args.periods is None:
        periods = calculate_num_periods(args.principal, args.payment, args.interest)
        years, months = divmod(periods, 12)
        message = generate_annuity_message(years, months)
        print(message)
        overpayment = ceil(args.payment * periods - args.principal)

    print(f'Overpayment = {overpayment}')