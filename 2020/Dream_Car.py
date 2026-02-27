def solve():
    salary = float(input()) #n
    month_expenses = float(input())#m
    sum_rises = float(input())#x
    car_price = float(input())#y
    months_saving = int(input())#t

    total_savings_per_month = salary - month_expenses
    last_month_savings = (salary + (months_saving - 1) * sum_rises) - month_expenses

    total_savings = (months_saving * (total_savings_per_month + last_month_savings)) / 2

    if total_savings >= car_price:
        print("Have a nice ride!")
    else:
        print("Work harder!")

solve()