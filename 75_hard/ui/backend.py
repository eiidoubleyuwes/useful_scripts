import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Parse input from frontend
    body = json.loads(event["body"])
    start_date = body["startDate"]
    include_daniel_fast = body["danielFast"]

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = start + timedelta(days=74)

    # Generate challenge content
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
    diet_daniel = "Follow Daniel Fast"
    diet_normal = "Follow clean, balanced diet"
    recipe = """
#### Daniel Fast Recipe
- Quinoa Veggie Bowl: Cook quinoa and top with sautéed vegetables, chickpeas, and a drizzle of olive oil.
"""

    content = f"# 75 Hard Challenge\n\n## Overview\n- **Start Date:** {start.strftime('%B %d, %Y')}\n- **End Date:** {end.strftime('%B %d, %Y')}\n\n---\n\n## Daily Logs\n"
    for day in range(75):
        current_date = start + timedelta(days=day)
        formatted_date = current_date.strftime("%B %d, %Y")
        day_num = day + 1
        diet = diet_daniel if include_daniel_fast and day < 21 else diet_normal
        content += daily_template.format(day_num=day_num, date=formatted_date, diet=diet)
        if include_daniel_fast and day < 21 and day == 0:  # Add recipe on Day 1
            content += recipe
        content += "\n---\n"

    # Return file content as a downloadable file
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/octet-stream",
            "Content-Disposition": "attachment; filename=75_Hard_Challenge.md",
        },
        "body": content,
        "isBase64Encoded": False,
    }
