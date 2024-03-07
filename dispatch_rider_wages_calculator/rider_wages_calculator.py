def calculate_rider_wages(number_of_delivery: int) -> int:
    if number_of_delivery < 50:
        return (number_of_delivery * 160) + 5_000
    if 50 < number_of_delivery < 60:
        return (number_of_delivery * 200) + 5_000
    if 50 < number_of_delivery < 60:
        return (number_of_delivery * 250) + 5_000
