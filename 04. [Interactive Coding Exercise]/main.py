# Write your code below this line 👇🏻
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(' FizzBuzz')

    elif number % 3 == 0:
        print(' Fizz')

    elif number % 5 == 0:
        print(' Buzz')

    else:
        print(number)
# Write your code above this line 👆🏻