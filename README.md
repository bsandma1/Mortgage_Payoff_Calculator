# Mortgage Payoff Calculator

Here we have a Python program that prompts the user for various inputs regarding their mortgage and then prints out a breakdown of how long it will take them to pay off their mortgage, based off of the answers provided within the prompts.

There are three Python files included, 1 main file that is used for executing the program and 2 supporting files that contain the functions which are called in the execution file.  All files must be present in the same directory to execute correctly.

- Mortgage_Payoff_Calculator.py (Execution file)
- Mortgage_Prompt.py (Supporting file) - Prompts the user for inputs and returns them as a list
- Mortgage_Calculations.py (Supporting file) - Takes the user inputs and does the main calculations

The user is prompted to provide...

- Remaining Loan Amount
- Interest Rate of the Loan
- Total Monthly Mortgage Payment 
- Monthly Escrow Costs (This will be a portion of the monthly mortgage)
- (Optional) Additional Principal Payment 

If you don't know any of these amounts, or you aren't sure, you can easily find all of these by logging into your mortgage loan account with whichever bank handles your mortgage loan.

I personally use this for a rental property I own to calculate if I want to pay extra towards the property every month!

NOTE: Not 100% complete, still need to test and correct for edge cases.