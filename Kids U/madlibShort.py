attempt = 5
for i in range(5):
    user_input = input('Enter Number: ')

    if user_input == "7":
        print('You won!')
        break
    else:
        attempt -= 1
        print('Try again!', attempt,' left.')
