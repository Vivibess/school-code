def time_input():
    while True:
        try:
                seconds = int(input("Enter total seconds: "))
                if seconds > 0:
                    break
                else:
                    print("Please try again")
        except ValueError:
            print("Please enter a valid number of seconds")
    return seconds

def tms(seconds):
    remaining_seconds = seconds % 60
    minutes = seconds // 60
    remaining_minutes = minutes % 60
    hours = minutes // 60
    remaining_hours = hours % 24
    time = [remaining_hours, remaining_minutes, remaining_seconds]
    return time

def format(time):
    time = [str(time[0]).zfill(2), str(time[1]).zfill(2), str(time[2]).zfill(2)]
    return time

def main():
    seconds = time_input()
    time = tms(seconds)
    formatted_time = format(time)
    print("The hours, minutes, and seconds for total seconds", seconds, "is", formatted_time[0] + ":" + formatted_time[1] + ":" + formatted_time[2])

main()