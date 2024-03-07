def calculate_rider_wages(number_of_deliveries: int) -> int:
    verify_number_of_deliveries(number_of_deliveries)
    return check_number_of_deliveries_and_return_wages(number_of_deliveries)


def check_number_of_deliveries_and_return_wages(number_of_deliveries: int) -> int:
    if number_of_deliveries == 0:
        return 5_000
    if number_of_deliveries < 50:
        return (number_of_deliveries * 160) + 5_000
    if 50 < number_of_deliveries < 60:
        return (number_of_deliveries * 200) + 5_000
    if 60 < number_of_deliveries < 70:
        return (number_of_deliveries * 250) + 5_000
    else:
        return (number_of_deliveries * 500) + 5_000


def verify_number_of_deliveries(number_of_deliveries: int) :
    if number_of_deliveries > 100 or number_of_deliveries < 0:
        raise ValueError("Invalid number of deliveries")
