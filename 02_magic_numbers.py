NUMBERS = ['3', '148', '74', '71', '4', '83', '95', '20', '61', '10', '69', '67', '23', '164', '97', '67', '144', '200', '38', '90', '200', '162', '6', '180', '65', '71', '90', '182', '16', '132', '182', '108', '90', '196', '48', '2', '158', '88', '39', '39', '54', '80', '89', '3', '90', '170', '88', '71', '142', '45', '81', '194', '36', '39', '30', '33', '38', '44', '134', '43', '12', '52', '170', '162', '192', '83', '18', '176', '120', '28', '86', '188', '51', '11', '96', '13', '198', '34', '66', '23', '200', '62', '194', '91', '51', '26', '152', '186', '86', '38', '46', '66', '83', '66', '40', '2', '20', '12', '91', '53']
user_number = 0

def cast_number_to_integer(number):
    return int(number)

def apply_user_number(number):
    return user_number * number

def convert_number_true(number):
    if number % 2 == 0:
        return True

user_number = int(input('Give me a number between 0 and 10'))

if user_number > 0 and user_number <= 10:
    # Logic
    integer_numbers = list(map(cast_number_to_integer, NUMBERS))
    integers_with_user_input = list(map(apply_user_number, integer_numbers))
    numbers_with_true = list(map(convert_number_true, integers_with_user_input))
    print(integer_numbers)
    print('\n')
    print(integers_with_user_input)
    print('\n')
    print(numbers_with_true)
