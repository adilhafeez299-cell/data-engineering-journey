#try:
  #  salary = int(input("Enter salary amount:"))
  #  days_qty = int(input("Enter days quantity: "))
  #  salary_per_day = round(salary / days_qty)
#except ValueError as e:
  #  print(e)
  #  print("cannot convert value to integer")
#except ZeroDivisionError as e:
  #  print(e)
  #  print("cannot divide by zero!")
#else:
    #print(salary_per_day)
   # print("Salary per day calculated successfully!")
   # print(f"my salary is {salary_per_day}, per day")

try:
    salary = int(input("Enter salary amount:"))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
except ValueError as e:
    print(e)
    print("cannot convert value to integer")
except ZeroDivisionError as e:
    print(e)
    print("cannot divide by zero!")
else:
    print("Result, salary per day", salary_per_day)
finally:
    print("Salary operation calculation complete")