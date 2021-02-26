from hours import work_day, total_hours
# PARAMETERS:
base_salary = 50
daily_hour = 10
food_budget = 100
total_sal = 0
counter = 1
days = work_day
while days > 0:
    for hours in total_hours:
        if hours <= daily_hour:
            salary = base_salary*hours + food_budget

        if daily_hour < hours <= 12:
            salary = daily_hour*base_salary + (hours-daily_hour)*1.25*base_salary + food_budget

        elif hours > 12:
            salary = daily_hour*base_salary + 2*1.25*base_salary + (hours-daily_hour-2)*1.5*base_salary + food_budget
        total_sal += salary
        days -= 1
        counter += 1

print("your salary is: {}".format(total_sal))

