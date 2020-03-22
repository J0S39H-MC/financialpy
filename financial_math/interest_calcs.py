def calculate_compound_interest(principal, rate, numberofperiods, time):
    amount = principal * ((1 + ((rate/numberofperiods))) ** (numberofperiods * time))
    return round(amount, 2)

def get_simple_compund_interest_schedule(principal, rate, numberofperiods, time):
    year = 1
    while (year < time * numberofperiods):
        principal = principal + (1 + rate)
        yield (year, round(principal, 2))
        year += 1
   

    



