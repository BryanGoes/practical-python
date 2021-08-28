# mortgage.py
#
# Exercise 1.7
# mortgage.py
 
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
month = 0
 
while principal > 0:
    month += 1
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        payment_n = payment + 1000
    else:
        payment_n = payment 
    principal = principal * (1+rate/12) - payment_n
    if principal < 0:
        payment_n += principal
        principal = 0
    total_paid = total_paid + payment_n
    print(month, total_paid, principal)
 
print('Total paid', total_paid)
print('Total month', month)
