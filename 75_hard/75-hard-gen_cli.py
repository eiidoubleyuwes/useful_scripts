# Generate the 75 Hard Challenge for all 75 days in the desired format for Obsidian.
from datetime import datetime, timedelta

start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=74)).strftime("%Y-%m-%d")


# Generate date range
start = datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.strptime(end_date, "%Y-%m-%d")
delta = (end - start).days + 1

# Build the checklist for each day
daily_template = """
### Day {day_num} - {date}
- **Morning Routine**
  - [ ] Wake up early
  - [ ] Read a chapter of a book

- **Physical Activity**
  - [ ] Workout indoors
  - [ ] Workout outdoors

- **Nutrition**
  - [ ] {diet}
  - [ ] Hydrate (Drink at least 3 liters of water)

- **Education**
  - [ ] School study
  - [ ] Personal study

- **Work & Creativity**
  - [ ] Project work
  - [ ] Ideation session

- **Reflection**
  - [ ] Reflect and log progress
"""

# Parameters for first 21 days
diet_daniel_fast = "Follow Daniel Fast"
diet_normal = "Follow clean, balanced diet"

# Generate the full text for all 75 days
output = f"# 75 Hard Challenge\n\n## Overview\n- **Start Date:** {start.strftime('%B %d, %Y')}\n- **End Date:** {end.strftime('%B %d, %Y')}\n\n---\n\n## Daily Logs\n"
for day in range(delta):
    current_date = start + timedelta(days=day)
    formatted_date = current_date.strftime("%B %d, %Y")
    day_num = day + 1
    diet = diet_daniel_fast if day < 21 else diet_normal  # Daniel Fast for first 21 days
    output += daily_template.format(day_num=day_num, date=formatted_date, diet=diet)
    output += "\n---\n"

# Save output to file for review
file_path = "/mnt/data/75_hard_obsidian_format.md"
with open(file_path, "w") as file:
    file.write(output)

file_path
