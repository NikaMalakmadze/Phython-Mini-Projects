#Time difference on the same day in seconds

hour1 = int(input(f"Please enter The Hour of the first(earlier) instant of time(No more than 24): "))
minute1 = int(input(f"Please enter The Minute of the first instant of time(No more than 60): "))
second1 = int(input(f"Please enter a Second of the first instant of time(No more than 60) "))

print("------------------------------------------------------------------------------------------")

hour2 = int(input(f"Please enter The Hour of the Second(later) instant of time(No more than 24): "))
minute2 = int(input(f"Please enter The Minute of the Second instant of time(No more than 60): "))
second2 = int(input(f"Please enter a Second of the Second instant of time(No more than 60): "))

hour_difference = (hour2 - hour1) * 3600            #converting hours to seconds
minute_difference = (minute2 - minute1) * 60        #coverting minutes to seconds
seconds_difference = second2 - second1

total_difference = abs(hour_difference + minute_difference + seconds_difference)         #summarize everything

print(f"The difference between these two periods of time in seconds is: " + str(total_difference) + "s")
