def find_available_time_to_min(schedule, workhours):
    # Create an empty list to store schedule and workhours
    availavle_time = []
    
    for time in schedule:
        availavle_time.extend(time)
    
    availavle_time.extend(workhours)

    # Convert time str to minutes
    def time_to_minutes(time_str):
        hour, min = map(int, time_str.split(':'))
        return hour * 60 + min
    
    min_arr = []

    for time_str in availavle_time:
        min = time_to_minutes(time_str)
        min_arr.append(min)

    min_arr.sort()

    return min_arr

def find_meeting_time(person1_available_time, person2_available_time, duration):
    meeting_time = []

    def minutes_to_time(min):
        hour = min // 60
        min = min % 60
        return f'{hour:02}:{min:02}'

    for person1_start, person1_end in zip(person1_available_time[::2], person1_available_time[1::2]):
        for person2_start, person2_end in zip(person2_available_time[::2], person2_available_time[1::2]):
            # When two time zones overlap
            if person1_end >= person2_start and person2_end >= person1_start:
                # Find overlap zone
                meeting_start = max(person1_start, person2_start)
                meeting_end = min(person1_end, person2_end)
                meeting_duration = meeting_end - meeting_start

                if meeting_duration >= duration:
                    meeting_time.append([minutes_to_time(meeting_start),minutes_to_time(meeting_end)])
    return meeting_time


input_file = 'input.txt'
output_file = 'output.txt'

# Read input.txt and get the data
with open(input_file, 'r') as file:
    lines = file.read().splitlines()
    line = 0 # For get the data by line

    # Write meeting_time to output.txt
    with open(output_file, 'w') as output_file:
        while line < len(lines):
            person1_busy_Schedule = eval(lines[0 + line])
            person1_work_hours = eval(lines[1 + line])
            person2_busy_Schedule = eval(lines[2 + line])
            person2_work_hours = eval(lines[3 + line])
            duration_of_meeting = int(lines[4 + line])

            person1_available_time = find_available_time_to_min(person1_busy_Schedule, person1_work_hours)
            person2_available_time = find_available_time_to_min(person2_busy_Schedule, person2_work_hours)
            meeting_time = find_meeting_time(person1_available_time, person2_available_time, duration_of_meeting)

            output_file.write(f'{meeting_time}\n')
            print(meeting_time)
            line += 6