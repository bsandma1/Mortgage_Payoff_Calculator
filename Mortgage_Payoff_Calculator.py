from Mortgage_Prompt import mortgage_prompt
from Mortgage_Calculations import mortgage_payoff_calculator

# Get user inputs from the mortgage_prompt() function in the form of a list
mortgage_inputs = mortgage_prompt()

# Unpack list inputs into the corresponding variables 
loan_principal = mortgage_inputs[0]
loan_interest_rate = mortgage_inputs[1]
monthly_mortgage_payment = mortgage_inputs[2]
monthly_escrow = mortgage_inputs[3]
additional_principal = mortgage_inputs[4]

# Plug values into the payoff calculator 
mortgage_payoff_calculator(loan_principal, loan_interest_rate, monthly_mortgage_payment,
                           monthly_escrow, additional_principal=additional_principal)
