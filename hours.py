# THIS TEXT FILES CONTAINS ALL THE LOG OF THE HOURS EVERY MONTH

month_hours = '*/FebHrs.txt'

"""This function calculates the hours of every given day"""
def get_salary_details(start, end):
    h1, m1 = start.split(':')
    h2, m2 = end.split(':')
    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1)
    m2 = int(m2)
    time_start = h1*60 + m1
    time_end = h2*60 + m2
    diff = time_end - time_start
    hours = int(diff / 60)
    minutes = int((diff % 60)/60 * 100)
    total_time = float(str(hours) + '.' +str(minutes))
    return total_time

# Reading the txt file with all the working dates and hours
with open(month_hours, 'r') as file:
    work_day = 0
    total_hours = []
    for line in file:
        line = line.split(' - ') # Splitting each parameter
        date, start_time, end_time = line # Unpacking all the parameters
        work_hours = get_salary_details(start_time, end_time)
        total_hours.append(work_hours)
        work_day += 1



