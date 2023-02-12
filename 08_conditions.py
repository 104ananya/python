is_hot = False
is_cold = True


if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its lovely day")

price = 100000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f'Down payment: ${down_payment}')
