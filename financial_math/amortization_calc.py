def calculate_interest(principal, rate, time):
    amount = float(principal) * (1 + int(rate) / 100) ** float(time)
    return amount

def get_money_time_value(principal, rate, time):
    current_value = principal
    schedule = {}
    for year in range(int(time)):
        current_value = calculate_interest(current_value, rate, year)
        schedule[year] = current_value
    return schedule


