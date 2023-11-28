#inputday =input("Enter the day : ")
#inputmodule= input("Enter your module name : ")





import pandas as pd

# Load the Excel sheet into a DataFrame
df = pd.read_excel('/Users/bijaygautam/Backups/Islington Files /5. Teaching Materials/Introduction to Information System/5. CC4058NI - Introduction to Information Systems - Autumn 2022/1. WorkLoad/Time Table - Resource Allocation Autumn 2023.xlsx', sheet_name='IT Year 1')

# Group the data by lecturer
lecturer_groups = df.groupby('Lecturer')

# Specify the module and lecturer for which you want to find free time
target_lecturer = 'Mr. Bijay Gautam'  # Replace with the desired lecturer's name
target_module = 'CS4571NI'  # Replace with the desired module code

# Filter the data for the target lecturer and module
target_data = df[(df['Lecturer'] == target_lecturer) & (df['Module Code'] == target_module)]

# Sort the data by the 'Day' and 'Time' columns
target_data = target_data.sort_values(by=['Day', 'Time'])

# Initialize variables to track the start and end times for free slots
start_time = '07:00 AM'
end_time = '07:00 AM'

# Iterate through the filtered data to find free time slots
free_time_slots = []
for index, row in target_data.iterrows():
    current_time = row['Time'].split(' - ')[1]
    if current_time > end_time:
        free_time_slots.append((end_time, current_time))
    end_time = row['Time'].split(' - ')[0]

# Display the free time slots
if len(free_time_slots) == 0:
    print(f"No free time slots found for {target_lecturer} and {target_module}.")
else:
    print(f"Free time slots for {target_lecturer} and {target_module}:")
    for start, end in free_time_slots:
        print(f"{start} - {end}")


