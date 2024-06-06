from math import ceil
def calculate_months(principal, monthly_payment):
    num_months = ceil(principal / monthly_payment)
    return num_months
def calculate_monthly_payment(principal, months):
    payments = {'monthly': ceil(principal / months)}

    if principal % months != 0:
        payments['last'] = principal - (months - 1) * payments['monthly']

    return payments

loan_principal = int(input('Enter the loan principal: '))
calculation_type = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for monthly payment:
''')

if calculation_type == "m":
    monthly_payment = int(input('Enter the monthly payment: '))
    num_months = calculate_months(loan_principal, monthly_payment)
    print(f'IT will take {num_months} month{"s" if num_months > 1 else ""} to repay the loan')

elif calculation_type == "p":
    months = int(input('Enter the number of months: '))
    monthly_payments = calculate_monthly_payment(loan_principal, months)

    result = f"Your monthly payment = {monthly_payments['monthly']}"
    if 'last' in monthly_payments:
        result += f' and the last payment = {monthly_payments["last"]}'

    print(result)