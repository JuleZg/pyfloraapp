import random


# LIGHT SENSOR READINGS

# Define the number of values to generate
num_values = 5

# Generate random light sensor values within the range of 0-100
light_values = [random.randint(0, 100) for i in range(num_values)]

# Grade the values based on the provided categories
grades = []
for value in light_values:
    if value < 20:
        grades.append("Low light intensity")
    elif value < 50:
        grades.append("Moderate light intensity")
    elif value < 80:
        grades.append("High light intensity")
    else:
        grades.append("Very high light intensity")

# Print the generated values and their grades
for i in range(num_values):
    print(
        f"Sample {i+1}: Light sensor reading = {light_values[i]}, Grade = {grades[i]}"
    )

sync_value_index = random.randint(0, num_values-1)
sync_value = light_values[sync_value_index]
sync_value_grade = grades[sync_value_index]

print(light_values)
print("-" * 150)


# SOIL HUMIDITY

# Define the soil humidity ranges in cb (centibars)
ranges = [
    {"label": "Over saturated soil", "min": 0, "max": 9},
    {"label": "Adequately moist", "min": 10, "max": 29},
    {"label": "Moderately dry, may require watering", "min": 30, "max": 60},
    {"label": "Very dry, in need of immediate watering.", "min": 61, "max": 99},
]

# Define the number of values to generate
num_values = 5

# Generate random soil humidity values within the specified ranges
humidity_values = []
for i in range(num_values):
    # Choose a random range and generate a value within that range
    range_idx = random.randrange(len(ranges))
    min_val = ranges[range_idx]["min"]
    max_val = ranges[range_idx]["max"]
    humidity_val = random.uniform(min_val, max_val)
    humidity_values.append(humidity_val)

# Print the generated values
for i in range(num_values):
    label = ""
    for r in ranges:
        if r["min"] <= humidity_values[i] <= r["max"]:
            label = r["label"]
            break
    print(f"Sample {i+1}: Soil Humidity = {humidity_values[i]:.2f} cb ({label})")
print(humidity_values)
print("-" * 150)

# PH & SALINITY
# Define the range of pH and salinity values
pH_range = (4.5, 8.5)
salinity_range = (0.1, 1.0)

# Define the number of values to generate
num_values = 5

# Generate random pH and salinity values within the specified range
pH_values = [random.uniform(pH_range[0], pH_range[1]) for i in range(num_values)]
salinity_values = [
    random.uniform(salinity_range[0], salinity_range[1]) for i in range(num_values)
]

# Grade the pH values based on the provided categories
pH_grades = []
for value in pH_values:
    if value < 5.5:
        pH_grades.append("Too acidic")
    elif value < 6.5:
        pH_grades.append("Neutral, ideal for most plants")
    elif value < 7.5:
        pH_grades.append("Slightly alkaline, acceptable for most plants")
    else:
        pH_grades.append("Too alkaline for most plants")

# Print the generated values and their grades
for i in range(num_values):
    print(
        f"Sample {i+1}: pH = {pH_values[i]:.2f} ({pH_grades[i]}), Salinity = {salinity_values[i]:.2f}"
    )
print(pH_grades)
