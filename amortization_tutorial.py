
# importing amortization
import amortization
# importing tabulate ( library to pretty-print data from python


from amortization.amount import  calculate_amortization_amount
# Example --> the percent needs to be in decimal form and the time in months!
# amount = calculate_amortization_amount(1500, 3.5/100, 42)
# print(amount)

# printing the amortization schedule example!
# from amortization.schedule import amortization_schedule
# for number,amount,interest,principal,balance in amortization_schedule(1500, 3.5/100, 24):
#     print(number, amount, interest, principal, balance)

from amortization.schedule import amortization_schedule
from tabulate import tabulate
table = (x for x in amortization_schedule(1500, 3.5/100, 24))
print(
    tabulate(
        table,
        headers=["Number", "Amount", "Interest", "Principal", "Balance"],
        floatfmt=",.2f",
        numalign="right"
    )
)


