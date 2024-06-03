# Завдання 1
# Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр. 
# Отриманий результат повертається з функції.

def Return_multiply_list(arr):
    multiply = 1
    for i in arr:
        multiply *= i
    return multiply

result = Return_multiply_list([1,2,3,4,5])
print(result)



# Завдання 2
# Напишіть функцію для знаходження мінімуму в списку цілих. Список передається як параметр. 
# Отриманий результат повертається з функції.

def Return_minimum_list(arr):
    minimal_value = min(arr)
    return minimal_value

result = Return_minimum_list([1,2,3,4,5])
print(result)



# Завдання 3
# Напишіть функцію, що визначає кількість простих чисел у списку цілих. Список передається як параметр. 
# Отриманий результат повертається з функції.

def Checking_prime_digit(arr):
    if arr <= 1:
        return False
    if arr <= 3:
        return True
    if arr % 2 == 0 or arr % 3 == 0:
        return False
    i = 5
    while i * i <= arr:
        if arr % i == 0 or arr % (i + 2) == 0:
            return False
        i += 6
    return True

def Return_count_primes(arr):
    primes = [i for i in arr if Checking_prime_digit(i)]
    return len(primes)

result = Return_count_primes([1,2,3,4,5])
print(result)



# Завдання 4
# Напишіть функцію, що видаляє зі списку цілих деяке задане число. З функції потрібно повернути кількість видалених елементів.

def Return_count_deleted(arr, deleted_digits):
    count = 0
    for num in arr:
        num_str = str(num)
        if all(str(digit) not in num_str for digit in deleted_digits):
            continue
        else:
            count += 1
    return count

result = Return_count_deleted([1,2,3,4,5], [1,2,3])
print(result)



# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

def Merge_lists(first_arr, second_arr):
    combine_arr = first_arr + second_arr
    return combine_arr

result = Merge_lists([1,2,3], [4,5,6])
print(result)



# Завдання 6
# Напишіть функцію, що обчислює ступінь кожного елемента списку цілих. 
# Значення для ступеня передається як параметр, список теж передається як параметр. 
# Функція повертає новий список, що містить отримані результати.

def Exponentiation_list(arr, degree):
    exponentiation_arr = [i**degree for i in arr]
    return exponentiation_arr

result = Exponentiation_list([1,2,3,4,5], 2)
print(result)