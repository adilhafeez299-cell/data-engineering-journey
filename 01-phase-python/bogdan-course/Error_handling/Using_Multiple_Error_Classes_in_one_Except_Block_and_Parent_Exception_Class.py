#try:
    #salary =int(input("Enter salary amount: "))
    #days_qty = int(input("Enter days quantity"))
    #salary_per_day = round(salary / days_qty)
    #print(salary_per_day)
#except (ValueError, ZeroDivisionError) as e:
   # print(e)
   # print(type(e))
    #print("some error occurred")

    # version 2

#try:
    #salary = int(input("Enter salary amount: "))
    #days_qty = int(input("Enter days quantity"))
    #salary_per_day = round(salary / days_qty)
    #print(salary_per_day)
#except (ValueError, ZeroDivisionError) as e:
   # if type(e) == ValueError:
  #      print(e)
        #print("Cannot convert value to int")
   #if type(e) == ZeroDivisionError:
      #  print(e)
      #  print("Cannot divide by zero")

#Example 3:
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity"))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except Exception as e:
    print(e)
    print(type(e))
    print(isinstance(e, Exception))
    print(isinstance(e, ValueError))
    print(isinstance(e, ZeroDivisionError))
    print("some error occurred")

#too broad exception clause, do not use except block without context
# use except exception as e:

# can have different except blocks for different error types
# try except block
#

