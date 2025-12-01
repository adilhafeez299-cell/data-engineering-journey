try:
    salary =int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity"))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")


#handling value error and ZeroDivisionError
