# mortgage.py
#
# Exercise 1.7
principal=500000.0
rate=0.05
payment=2684.11
total_paid=0.0
months=0
extra_payment_start_month=int(input('enter start month:'))
extra_payment_end_month=int(input('enter end month:'))
extra_payment=int(input('enter extra payment:'))
while principal > 0:
    if months>=extra_payment_start_month and months<extra_payment_end_month:
        if principal<(payment+extra_payment):
            total_paid = total_paid + principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - (payment+extra_payment)
            total_paid = total_paid + payment+extra_payment
        months+=1
        print(f'{months} {total_paid:0.2f} {principal:0.2f}')
        
    else:
        if principal<(payment+extra_payment):
            total_paid = total_paid + principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
        months+=1
        print(f'{months} {total_paid:0.2f} {principal:0.2f}')
     
print(f'Total paid {total_paid:0.2f}')
print(f'number of months req {months}')
