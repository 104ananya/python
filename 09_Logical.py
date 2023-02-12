high_income = True
good_credit = True
is_fit = False
is_criminal = False

if high_income and good_credit:
    print("Eligible for loan")

if high_income or is_fit:
    print("yes")

if high_income and not is_criminal:
    print("Ofcourse")

