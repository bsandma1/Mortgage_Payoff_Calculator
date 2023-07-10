# Function for recieving input from user

def mortgage_prompt():
    print(f'\nHi!  Welcome to the Mortgage Payoff Calculator!\n')
    print(f'You will be prompted to enter some personal information about your mortgage, make sure to enter the information in the correct format!\n')
    print(f'All of the required information can be found on the bank\'s website in which you took out the mortgage from! (Your Mortgage Account)\n')

    print(f'Proper Format: 295750.74 | Improper Format(s): $295,750.74')
    loan_principal = float(
        input('What is the current balance remaining on your mortgage?\n\n'))

    print(f'\nProper Format: 7.25 | Improper Format(s): 7.25% or 0.0725')
    loan_interest_rate = float(
        input('What is the interest rate on your mortgage?\n\n'))

    print(f'\nProper Format: 2259.43 | Improper Format(s): $2,259.43')
    monthly_mortgage_payment = float(
        input('What is the total monthly mortgage payment?\n\n'))

    print(f'\nProper Format: 456.77 | Improper Format(s): $456.77')
    monthly_escrow = float(
        input('What is the monthly escrow payment? (This is your monthly taxes and insurance payment)\n\n'))

    print(f'\nProper Format: 1000 | Improper Format(s): $1,000')
    additional_principal = input(
        'What is the additional amount you\'d like to pay monthly towards your principal? (Enter \'0\' if you don\'t want to pay any additional payment)\n\n')

    if additional_principal == '0':
        additional_principal = None
    else:
        additional_principal = float(additional_principal)

    return [loan_principal, 
            loan_interest_rate,
            monthly_mortgage_payment,
            monthly_escrow,
            additional_principal]