import math

def next_palindrome(number):
    length_of_number = len(str(number))
    mid_index = math.floor(length_of_number/2)
    number_string = str(number)
    
    if length_of_number % 2 == 1:
        next_pal = number_string[mid_index]
        if number_string[mid_index - 1] <= number_string[mid_index + 1]:
                next_pal = str((int(next_pal) + 1) % 10)
        for i in range(1, mid_index + 1):
            next_pal = number_string[mid_index - i] + next_pal + number_string[mid_index - i]
    else:
        next_pal = number_string[mid_index - 1]
        next_pal = (int(next_pal) + 1) % 10
        next_pal = str(next_pal) * 2
        for i in range(2, mid_index + 1):
            next_pal = number_string[mid_index - i] + next_pal + number_string[mid_index - i]
            
    print(int(next_pal))

next_palindrome(123)
next_palindrome(808)
next_palindrome(777)
next_palindrome(1001)
next_palindrome(12345)
next_palindrome(987654321)
next_palindrome(3**39)