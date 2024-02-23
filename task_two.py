def sum_even_and_odd_number(number):
    list1 = []
    odd_sum = 0
    even_sum = 0
    for num in range(1,number):
        if num%2 == 0: even_sum += num
        else: odd_sum += num
    list1.append(even_sum)
    list1.append(odd_sum)
    return list1

def sum_even_and_odd_number_one(number):
    return f"sum of even number is {sum(filter(lambda x: x % 2 == 0, range(number)))} sum of odd numbers is {sum(filter(lambda x: x % 2 == 1, range(number)))}"

number2 = 15
print(sum_even_and_odd_number_one(15))