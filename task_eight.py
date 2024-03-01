def collect_input(*args):
    expected_result = ""
    num = len(args)
    for number in range(num):
        if number == num-1:
            expected_result += str(int(((2*50*args[number])/30)**0.5//1))
        else:
            expected_result += str(int(((2*50*args[number])/30)**0.5//1))
            expected_result += ","
    return expected_result


print(collect_input(100,150,180))