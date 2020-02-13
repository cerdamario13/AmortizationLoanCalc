
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta  # for adding time in months/years
from tabulate import tabulate

# known values ###########################################
principal = 1333  # this is the starting point
interest = 3.15  # yearly - convert to monthly
int_per_month = (3.15/100) / 12
months = 89
month_pmt = 16.85
Year = 2020
Month = 1
Day = 11
##########################################################

DATE = datetime.datetime(Year, Month, Day)
int_1st_month = principal * int_per_month * 1  # interest for 1st month
principal_1st_PMT = month_pmt - int_1st_month
ending_principal_test = principal - principal_1st_PMT
# print(int_1st_month)
# print(principal_1st_PMT)
# print(ending_principal)

principal_ = []
interest_pmt = []
principal_pmt = []
ending_principal = []
end_month_list = []
end_year_list = []

for i in range(0, months):
    interest_loop = principal * int_per_month * 1  # interest payed each payment
    principal_pmt_loop = month_pmt - interest_loop  # payment that goes to the principal
    # notice how principal is on both sides of equation
    principal = principal - principal_pmt_loop  # new principal after the month
    end_date = DATE + relativedelta(months=i)

    # populating the lists
    principal_.append(round(principal + principal_pmt_loop, 2))
    interest_pmt.append(round(interest_loop, 2))
    principal_pmt.append(round(principal_pmt_loop, 2))
    ending_principal.append(round(principal, 2))
    end_month_list.append(end_date.strftime("%B"))
    end_year_list.append(end_date.strftime("%Y"))

    # print(i, round(principal + principal_pmt_loop, 2), round(interest_loop, 2),
    #       round(principal_pmt_loop, 2), round(principal, 2), end_date.strftime("%B " "%Y"))

# ending for loop

# converting list to numpy arrays
principal_np = np.asarray(principal_)
interest_pmt_np = np.asarray(interest_pmt)
principal_pmt_np = np.asarray(principal_pmt)
ending_principal_np = np.asarray(ending_principal)
end_month_np = np.asarray(end_month_list)
end_year_np = np.asarray(end_year_list)

# printing the data using 'Tabulate'
# print(tabulate([[np.vstack(principal_),
#                  np.vstack(interest_pmt),
#                  np.vstack(principal_pmt_np),
#                  np.vstack(ending_principal_np),
#                  np.vstack(end_month_np),
#                  np.vstack(end_year_np)]],
#                headers=['Principal', 'Interest PMT',
#                         'Principal PMT', 'Ending Principal', 'Month', 'Year'],
#                tablefmt='simple',
#                numalign='right'
#                ))
# END print tabulate

# Searching for data (Time till pay off, last payment, etc...)
last_loc = np.where(ending_principal_np < 0)  # last payment, should be negative number
# Based on the location of the last payment, look for the DATE when it is payed
last_payment = ending_principal_np[last_loc]
payed_month = str(end_month_np[last_loc]).lstrip('[').rstrip(']')
payed_year = end_year_np[last_loc]

# print("Month payed: ", payed_month)
# print(str(ending_principal_np[last_loc]).lstrip('[').rstrip(']'))
# top is how to get rid of the brackets in the array

# Printing the results
print('Loan payed in ', str(payed_month), payed_year)



