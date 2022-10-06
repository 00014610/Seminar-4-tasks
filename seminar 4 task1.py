def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    if n >= 0:
        print('Blasstoff')
    else:
        print(n)
        countup(n+1)


while True:
    try:
        user_numer = int(input('Write a number here: '))
        break
    except ValueError:
        print('it is not a number')


if user_numer < 0:
    countup(user_numer)
elif user_numer > 0:
    countdown(user_numer)
else:
    countdown(user_numer)


