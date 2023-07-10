# Function for making main calculations

def mortgage_payoff_calculator(loan_principal, loan_interest_rate, monthly_mortgage_payment, monthly_escrow, additional_principal=None):

    original_loan_amount = loan_principal

    # Convert interest rate percentage to decimal
    loan_interest_rate /= 100

    # Counter
    months_to_pay_off = 0

    while loan_principal > 0:

        monthly_interest = round((loan_principal * loan_interest_rate) / 12, 2)
        monthly_principal = round(monthly_mortgage_payment - monthly_interest - monthly_escrow, 2)
        loan_principal -= monthly_principal
        if additional_principal:
            loan_principal -= additional_principal
        months_to_pay_off += 1

    years_to_pay_off = round(months_to_pay_off / 12, 2)

    print('\n---\n')
    print(f'Loan Amount: ${original_loan_amount}')
    print(f'Interest Rate: {loan_interest_rate * 100}%')
    print(f'Monthly Taxes and Insurance: ${monthly_escrow}')
    print(f'Monthly Payment: ${monthly_mortgage_payment}')
    
    if additional_principal:
        
        print(f'Additional Monthly Payment: ${additional_principal} (Paid Towards the Principal)')
        print(f'Total Monthly Payment: ${monthly_mortgage_payment + additional_principal}')
        print(f'\nAt a rate of ${monthly_mortgage_payment + additional_principal} a month, with a loan principal of ${original_loan_amount} and an interest rate of {loan_interest_rate * 100}%, it will take {years_to_pay_off} years to pay off your mortgage. ({round(2023 + years_to_pay_off)})')
    
    else:
        
        print(f'\nAt a rate of ${monthly_mortgage_payment} a month, with a loan principal of ${original_loan_amount} and an interest rate of {loan_interest_rate * 100}%, it will take {years_to_pay_off} years to pay off your mortgage. ({round(2023 + years_to_pay_off)})')
