
# importing amortization
import amortization
# importing tabulate ( library to pretty-print data from python

from amortization.schedule import amortization_schedule
from tabulate import tabulate

# known values
principal = 1333
interest = 3.15
months = 12

table = (x for x in amortization_schedule(principal, interest/100, months))
print(
    tabulate(
        table,
        headers=["Number", "Amount", "Interest", "Principal", "Balance"],
        floatfmt=",.2f",
        numalign="right"
    )
)



