from random import randint


def generate_user_id():
    """ Keeps looping until it finds a valid id """

    while True:
        new_id = _generate_random_id()
        if _check_id_validity(new_id):
            return int_list_to_string(new_id)


def _generate_random_id():
    first_number = randint(1, 9)  # generates 1 random number between 1 and 9
    number_list = [randint(0, 9) for _ in range(9)]  # generates list of 9 random numbers between 0 and 9
    number_list.insert(0, first_number)  # joins all numbers to create a list of 10 numbers
    return number_list


def _check_id_validity(number_list):
    sum_digits = sum(number_list[:-1])
    if sum_digits % 10 == number_list[-1]:  # checks the sum of the numbers against the last digit modulo 10
        return True
    else:
        return False


def _int_list_to_string(int_list):
    string_ints = [str(number) for number in int_list]
    return "".join(string_ints)
