# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0.0:
    monthly_payment = payment
    if total_months <= extra_payment_end_month and total_months >= extra_payment_start_month:
        monthly_payment += extra_payment
    if float(monthly_payment) > principal * (1+rate/12):
        monthly_payment = principal
    principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    total_months += 1
    print(round(total_months,2), round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2))
print('Total months', round(total_months,2))