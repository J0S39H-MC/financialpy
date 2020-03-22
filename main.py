from financial_math import interest_calcs as calculator

payment_amount =  calculator.calculate_compound_interest(5000,0.05,12,10)
print(payment_amount)

for period in calculator.get_simple_compund_interest_schedule(5000,0.05, 12, 10):
    print(period)



